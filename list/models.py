from django.db import models

from django.contrib.auth.models import User

user=User
# Create your models here.
class Item(models.Model):
    item=models.CharField (max_length=200)
    description=models.TextField (max_length=900)
    completed=models.BooleanField(default=False)
    created=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.item
