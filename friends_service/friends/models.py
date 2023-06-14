from django.db import models

class User(models.Model):
    """
    Модель пользователя социальной сети
    """
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=255)
    friends = models.ManyToManyField('self', blank=True)

class FriendRequest(models.Model):
    """
    Модель заявки в друзья
    """
    PENDING = 'pending'
    ACCEPTED = 'accepted'
    DECLINED = 'declined'

    STATUS_CHOICES = [
        (PENDING, 'Pending'),
        (ACCEPTED, 'Accepted'),
        (DECLINED, 'Declined'),
    ]

    id = models.AutoField(primary_key=True)
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_friend_requests')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_friend_requests')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=PENDING)
