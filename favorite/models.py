from django.db import models
from user.models import CustomUser

class Favorite(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    link = models.CharField(max_length=255)
    favo_at = models.DateTimeField(auto_now=True)
    is_delete = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title