from django.db import models
from main_Users .models import *


class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sent_message", blank=True, null=True)
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name="received_message", blank=True, null=True)
    text = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self) -> str:
        return f'{self.sender} || {self.receiver}'