from django.db import models
from django.contrib.auth.models import User

class Friend (models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, related_name= "user", null=False, on_delete=models.CASCADE)
    friend = models.ForeignKey(User, related_name= "friend", null=False, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['user', 'friend']

class FriendRequest (models.Model):
    id = models.BigAutoField(primary_key=True)
    requested_by = models.ForeignKey(User, null=False, related_name="requested_by", on_delete=models.CASCADE)
    requested_to = models.ForeignKey(User, null=False, related_name="requested_to", on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['requested_by', 'requested_to']