from django.db import models
from django.db.models import Sum
from django.contrib.auth.models import User


class Currency(models.Model):
    abbreviation = models.CharField(max_length=3)
    symbol = models.CharField(max_length=1)
    extra = models.CharField(max_length=64, blank=True, null=True)

    def __str__(self):
        return '{a}, {s}'.format(a=self.abbreviation, s=self.symbol)


class Account(models.Model):
    name = models.CharField(max_length=64)
    owner = models.ForeignKey(User)
    currency = models.ForeignKey(Currency)

    @property
    def total(self):
        _sum = self.transaction_set.filter(account=self, user=self.owner).aggregate(Sum('value'))['value__sum']
        return _sum or 0.0

    def editable_for(self, user):
        """Check if user can edit account (transactions)."""
        return user == self.owner

    def __str__(self):
        return '{n} ({o})'.format(n=self.name, o=self.owner)


class Transaction(models.Model):
    value = models.FloatField()
    account = models.ForeignKey(Account)
    user = models.ForeignKey(User)
    created_at = models.DateTimeField(auto_now=True)
    comment = models.TextField(blank=True, null=True)

    def __str__(self):
        return '{c}{v}, {a}'.format(c=self.account.currency.symbol, v=self.value, a=self.account)
