from django.db import models

# Create your models here.
from django.contrib.auth.models import User





class userMessage(models.Model):
    text = models.CharField(max_length=3000)
    sender = models.ForeignKey(to=User,on_delete=models.CASCADE)
    # sender_contact = models.IntegerField(
    def __str__(self):
        return str(self.sender)
    
class adminMessage(models.Model):
    admintext = models.CharField(max_length=4000)
    receiver = models.OneToOneField(userMessage, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.receiver)