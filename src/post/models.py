from django.db import models
from django.contrib.auth.models import User

class Post (models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    hint_or_question = models.CharField(max_length=255, null=False)
    answer = models.TextField(null=False)
    option1 = models.TextField(null=False)
    option2 = models.TextField(null=False)
    option3 = models.TextField(null=True, blank=True)
    option4 = models.TextField(null=True, blank=True)

    likes = models.IntegerField(default=0, null=False, blank=False)

    created_at = models.DateTimeField(auto_now_add=True)
    is_revealed = models.BooleanField(default=False, null=False)

    def __str__ (self):
        return f"{self.hint_or_question}."
    

class PostPrediction (models.Model):
    id = models.BigAutoField(primary_key=True)
    post = models.ForeignKey(Post, related_name= "post", null=False, on_delete=models.CASCADE)
    post_of = models.ForeignKey(User, related_name= "post_of", null=False, on_delete=models.CASCADE)
    prediction_of = models.ForeignKey(User,related_name= "prediction_of", null=False, on_delete=models.CASCADE)
    prediction = models.TextField(null=False)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['post_of', 'prediction_of']

    def __str__ (self):
        return f"{self.post} prediction of {self.prediction_of} and prediction is {self.prediction}."
    
