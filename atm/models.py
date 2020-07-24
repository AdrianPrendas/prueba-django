from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    date = models.DateTimeField(auto_now_add=True)
    amount = models.IntegerField()

