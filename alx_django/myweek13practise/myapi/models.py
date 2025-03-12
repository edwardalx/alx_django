from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Player(models.Model):
    player = models.ForeignKey(User, on_delete=models.CASCADE)
    balance = models.IntegerField()

class Customer(User):
    ...