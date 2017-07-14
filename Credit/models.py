from django.contrib.auth.models import User
from django.core.validators import RegexValidator, MinLengthValidator
from django.db import models

# Create your models here.


class CreditCard(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    name_on_card = models.CharField(max_length=64)
    type = models.CharField(max_length=32)
    expiry_date = models.CharField(max_length=16)
    number = models.CharField(max_length=16)
    owner = models.ForeignKey(User)

    def __str__(self):
        return self.first_name+" "+self.last_name

