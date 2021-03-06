from django.db import models as db_models
from django.db.models.fields import related
from django.contrib.auth import models as auth_models

from . import constants

# Create your models here.


class Account(db_models.Model):
    uuid = db_models.UUIDField()
    user = db_models.ForeignKey(auth_models.User)
    
    def __str__(self):
        return str(self.uuid)

class CurrencyType(db_models.Model):
    name = db_models.CharField(max_length=256, unique=True)
    
    def __str__(self):
        return self.name

# TODO: Validate that two saving boxes that belongs from the same account 
# can not have the same currency_type.
class SavingBox(db_models.Model):
    currency_type = related.ForeignKey(CurrencyType)
    account = related.ForeignKey(Account)
    
    @property
    def balance(self):
        moves = Move.objects.filter(saving_box=self)
        balance = sum(map(lambda move: 
            move.amount if constants.MoveType[move.typee] == constants.MoveType.DEPOSIT else -move.amount, 
            moves))
        return balance
    
    def __str__(self):
        return '{currency_type} saving box of {account}'.format(
            currency_type=self.currency_type,
            account=self.account,
        )

class Cause(db_models.Model):
    name = db_models.CharField(max_length=256)
    description = db_models.CharField(max_length=256, blank=True)
    
    def __str__(self):
        return self.name

class Move(db_models.Model):
    typee = db_models.CharField(max_length=256, choices=(
        (constants.MoveType.DEPOSIT.name, 'DEPOSIT'),
        (constants.MoveType.EXTRACTION.name, 'EXTRACTION'), ))
    description = db_models.CharField(max_length=256, blank=True)
    date = db_models.DateTimeField()
    cause = db_models.ForeignKey(Cause)
    saving_box = db_models.ForeignKey(SavingBox)
    amount = db_models.FloatField()
    
    def __str__(self):
        return '{typee} of ${amount} {direction} {saving_box} due to {cause} at {date}'.format(
            typee=self.typee,
            amount=self.amount,
            direction=constants.MoveType[self.typee] == constants.MoveType.DEPOSIT and 'in' or 'from',
            saving_box=self.saving_box,
            cause=self.cause,
            date=self.date,
         )