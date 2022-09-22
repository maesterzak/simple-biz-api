from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Orders(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    transaction_id = models.CharField(max_length=200)
    total = models.IntegerField()
    date_time = models.DateTimeField(auto_now_add=True, blank=True)


    