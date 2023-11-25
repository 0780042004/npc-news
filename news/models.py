#from fcntl import DN_DELETE
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class post(models.Model):
    title=models.CharField(max_length=40)
    content=models.TextField(max_length=400)
    date=models.DateField(auto_now_add=True)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.title} created by {self.user.username}" 
