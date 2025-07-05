from django.db import models

# Create your models here.
class Signup(models.Model):
    username=models.CharField()
    email=models.EmailField()
    password=models.CharField()
    
    def __str__(self):
        return self.username
    
    
class Chat(models.Model):
    sender = models.ForeignKey(Signup, on_delete=models.CASCADE, related_name='sent_messages')
    receiver = models.ForeignKey(Signup, on_delete=models.CASCADE, related_name='received_messages')
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    # def __str__(self):
    #     return f"{self.sender.username} to {self.receiver.username}: {self.message}"
    
