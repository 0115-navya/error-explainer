from django.db import models
from django.contrib.auth.models import User

class ErrorExplanation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    error_text = models.TextField()          
    language = models.CharField(max_length=50, default='Unknown')  # Python, JS etc
    severity = models.CharField(max_length=20, default='Error')    # Warning/Error/Critical
    explanation = models.TextField()         # AI's response
    created_at = models.DateTimeField(auto_now_add=True)  # timestamp

    def __str__(self):
        return f"{self.user.username} - {self.language} - {self.created_at}"