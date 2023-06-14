from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import User, FriendRequest
from .serializers.serializers import UserSerializer, FriendRequestSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(detail=True, methods=['get'])
    def friends(self, request, pk=None):
        user = self.get_object()
        friends = user.friends.all()
        serializer = UserSerializer(friends, many=True)
        return Response(serializer.data)



    @action(detail=True, methods=['post'])
    def remove_friend(self, request, pk=None):
        user = self.get_object()
        friend_id = request.data.get('friend_id')
        try:
            friend = User.objects.get(id=friend_id)
        except User.DoesNotExist:
            return Response({'message': 'Invalid friend ID'})

        user.friends.remove(friend)

        return Response({'message': 'Friend removed successfully'})


class FriendRequestViewSet(viewsets.ModelViewSet):
    queryset = FriendRequest.objects.all()
    serializer_class = FriendRequestSerializer

    @action(detail=False, methods=['post'])
    def send_friend_request(self, request):
        sender_id = request.data.get('sender')
        receiver_id = request.data.get('receiver')

        try:
            sender = User.objects.get(id=sender_id)
        except User.DoesNotExist:
            return Response({'message': 'Invalid sender ID'})

        try:
            receiver = User.objects.get(id=receiver_id)
        except User.DoesNotExist:
            return Response({'message': 'Invalid receiver ID'})

        if sender == receiver:
            return Response({'message': 'Cannot send friend request to yourself'})

        if FriendRequest.objects.filter(sender=sender, receiver=receiver).exists():
            return Response({'message': 'Friend request already sent'})

        if FriendRequest.objects.filter(sender=receiver, receiver=sender).exists():
            # Auto-accept the friend request if both users sent requests to each other
            FriendRequest.objects.filter(sender=receiver, receiver=sender).update(status=FriendRequest.ACCEPTED)
            return Response({'message': 'Friend request accepted'})

        friend_request = FriendRequest(sender=sender, receiver=receiver)
        friend_request.save()

        return Response({'message': 'Friend request sent successfully'})

    @action(detail=True, methods=['post'])
    def accept_friend_request(self, request, pk=None):
        friend_request = self.get_object()

        if friend_request.status != FriendRequest.PENDING:
            return Response({'message': 'Invalid friend request status'})

        friend_request.status = FriendRequest.ACCEPTED
        friend_request.save()

        return Response({'message': 'Friend request accepted'})

    @action(detail=True, methods=['post'])
    def decline_friend_request(self, request, pk=None):
        friend_request = self.get_object()

        if friend_request.status != FriendRequest.PENDING:
            return Response({'message': 'Invalid friend request status'})

        friend_request.status = FriendRequest.DECLINED
        friend_request.save()

        return Response({'message': 'Friend request declined'})

    @action(detail=False, methods=['get'])
    def outgoing_friend_requests(self, request):
        user = request.user
        outgoing_requests = FriendRequest.objects.filter(sender=user)
        serializer = self.get_serializer(outgoing_requests, many=True)

        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def incoming_friend_requests(self, request, username):
        user_id = request.query_params.get('user_id')
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return Response({'message': 'Invalid user ID'})

        incoming_requests = FriendRequest.objects.filter(receiver=user)
        serializer = self.get_serializer(incoming_requests, many=True)

        return Response(serializer.data)

