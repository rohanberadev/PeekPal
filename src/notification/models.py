from pyexpat import model
from django.db import models
from django.contrib.auth.models import User
from friends.models import FriendRequest
from post.models import Post, PostPrediction

class FreindRequestNotification (models.Model):
    id = models.BigAutoField(primary_key=True)
    friend_request = models.ForeignKey(FriendRequest, on_delete=models.CASCADE, related_name="friend_request")
    send_from = models.ForeignKey(User, on_delete=models.CASCADE, related_name="send_request_from", null=False)
    send_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name="send_request_to", null=False)  
    status = models.CharField(max_length=20, choices=[('ACCEPT', 'accept'), ('DECLINE', 'decline'), ('PENDING', 'pending')], default="pending", null=False, blank=False)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['send_from', 'send_to']


class FriendPostNotification (models.Model):
    id = models.BigAutoField(primary_key=True) 
    send_from = models.ForeignKey(User, on_delete=models.CASCADE, related_name="send_post_from", null=False)
    send_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name="send_post_to", null=False)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=False)
    is_post_reveled = models.BooleanField(null=False, blank=False, default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['send_from', 'send_to']


class FriendPostPredictionNotification (models.Model):
    id = models.BigAutoField(primary_key=True) 
    send_from = models.ForeignKey(User, on_delete=models.CASCADE, related_name="send_post_prediction_from", null=False)
    send_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name="send_post_prediction_to", null=False)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=False)
    post_predition = models.ForeignKey(PostPrediction, on_delete=models.CASCADE, related_name="post_predition", null=False)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['send_from', 'send_to']