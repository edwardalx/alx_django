from django.db import models
from django.contrib.auth.models import AbstractUser, User, Group, Permission


# Create your models here.
class Player(models.Model):
    player = models.ForeignKey(User, on_delete=models.CASCADE)
    balance = models.IntegerField()

class Customer(AbstractUser):
    phoneNumber = models.CharField(unique=True, primary_key=True, max_length=13)
    username = None
    USERNAME_FIELD = "phoneNumber"
    REQUIRED_FIELDS = ["phoneNumber",'first_name', 'last_name', 'password']
    groups = models.ManyToManyField(Group, related_name="customer_groups", blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name="customer_permissions", blank=True)
    def __str__(self):
        return f"Name: {self.first_name}  Mobile:{self.phoneNumber} "