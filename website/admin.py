from django.contrib import admin
from website.models import Currency, Account, Transaction
import functools


admin.site.register(Currency)
admin.site.register(Account)
admin.site.register(Transaction)
