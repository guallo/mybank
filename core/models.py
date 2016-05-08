from django.db import models
from django.contrib.auth.models import User

from .constants import MoveType
from django.db.models.fields.related import ForeignKey

# Create your models here.

class Account(models.Model):
    user = models.ForeignKey(User)

class CurrencyType(models.Model):
    name = models.CharField(max_length=256)

class SavingBox(models.Model):
    currency_type = ForeignKey(CurrencyType)
    account = ForeignKey(Account)

class Cause(models.Model):
    name = models.CharField(max_length=256)
    description = models.CharField(max_length=256)

class Move(models.Model):
    typee = models.IntegerField(choices=((MoveType.DEPOSIT.value, 'DEPOSIT'),
                                         (MoveType.EXTRACTION.value, 'EXTRACTION'), ))
    description = models.CharField(max_length=256)
    date = models.DateTimeField()
    cause = models.ForeignKey(Cause)
    saving_box = models.ForeignKey(SavingBox)
    amount = models.FloatField()