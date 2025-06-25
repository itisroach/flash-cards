from django.db import models
from django.contrib.auth import get_user_model

class Card(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    
    question = models.TextField()
    
    answer = models.TextField()
    
    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True) 


    def __str__(self):
        return f"{self.question[:10]}..."