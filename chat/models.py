from django.db import models
from django.contrib.auth.models import User

class Message(models.Model):
    message = models.TextField()
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
