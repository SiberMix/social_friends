from django.urls import path, include
from rest_framework import routers
from .views import UserViewSet, FriendRequestViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'friend-requests', FriendRequestViewSet)



urlpatterns = [
    path('', include(router.urls)),
]
