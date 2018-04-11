from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView  #, CreateView, UpdateView, DeleteView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.http import Http404, HttpResponseForbidden
from .models import Account
from .mixins import LoginRequiredMixin
from .forms import IncomeTransactionForm, ExpenditureTransactionForm


class AccountListView(LoginRequiredMixin, ListView):
    template_name = 'account-list.html'
    model = Account

    def get(self, request, *args, **kwargs):
        self.queryset = self.model.objects.filter(owner=request.user)
        super().get(request, *args, **kwargs)
        return self.render_to_response(self.get_context_data())


class AccountCreateView(LoginRequiredMixin, CreateView):
    template_name = 'account-form.html'
    model = Account
    success_url = reverse_lazy('account_list')
    fields = ['name', 'currency']

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.owner = self.request.user
        self.object.save()
        return super().form_valid(form)


class AccountUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'account-form.html'
    model = Account
    success_url = reverse_lazy('account_list')
    fields = ['name', 'currency']


class AccountDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'account-delete.html'
    model = Account
    success_url = reverse_lazy('account_list')


class TransactionFormView(FormView):
    template_name = 'account-transaction-form.html'
    success_url = reverse_lazy('account_list')

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        account = Account.objects.filter(pk=kwargs.get('account_id', None)).first()

        if not account:
            raise Http404('Account not found')
        if not account.editable_for(request.user):
            return HttpResponseForbidden('Permission denied')

        if form.is_valid():
            form.save(user=request.user, account=account)

        return super().post(request, *args, **kwargs)


class IncomeTransactionFormView(TransactionFormView):
    form_class = IncomeTransactionForm


class ExpenditureTransactionFormView(TransactionFormView):
    form_class = ExpenditureTransactionForm
