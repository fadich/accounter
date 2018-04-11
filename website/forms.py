from django.forms import ModelForm
from django.core.validators import MinValueValidator
from .models import Transaction


class TransactionForm(ModelForm):

    class Meta:
        model = Transaction
        exclude = (
            'user',
            'account',
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields.get('value').validators.append(MinValueValidator(0.01))

    def save(self, commit=True, user=None, account=None):
        self.instance.user = user
        self.instance.account = account

        return super().save(commit)


class IncomeTransactionForm(TransactionForm):
    pass


class ExpenditureTransactionForm(TransactionForm):

    def save(self, commit=True, user=None, account=None):
        self.instance.value = self.cleaned_data.get('value') * -1

        return super().save(commit, user, account)
