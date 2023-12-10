from django.contrib.auth.models import User
from django.db import models

class Group(models.Model):
    name = models.CharField(max_length=100)
    members = models.ManyToManyField(User)

    def __str__(self):
        return self.name

class Chat(models.Model):
    participants = models.ManyToManyField(User, related_name='chats')
    is_group_chat = models.BooleanField(default=False)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, null=True, blank=True)
    message = models.CharField(max_length=255, blank=True)
    reply_message = models.TextField(blank=True, null=True)
    # Add any other fields like timestamp, etc.

    def __str__(self):
        return f"Chat {self.id}"
