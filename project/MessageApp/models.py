from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class PrivateMessage(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages', editable=True)
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
    message = models.TextField()
    time = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return str(self.recipient)
    # def save(self, *args, **kwargs):
    #     if not self.pk:
    #         # Set the sender as the logged-in user if it's a new instance
    #         self.sender = User.objects.get(pk=self.sender_id)
    #     super().save(*args, **kwargs)

