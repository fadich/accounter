from django.conf.urls import url
from website.views import AccountListView, AccountCreateView, AccountUpdateView, AccountDeleteView, \
    IncomeTransactionFormView, ExpenditureTransactionFormView
from website.api.views import AccountViewSet
from rest_framework.routers import DefaultRouter


urlpatterns = [
    url(r'^$', AccountListView.as_view(), name='account_list'),
    url(r'^new$', AccountCreateView.as_view(), name='account_new'),
    url(r'^edit/(?P<pk>\d+)$', AccountUpdateView.as_view(), name='account_edit'),
    url(r'^delete/(?P<pk>\d+)$', AccountDeleteView.as_view(), name='account_delete'),
    url(r'^(?P<account_id>\d+)/income-transactions/new$', IncomeTransactionFormView.as_view(),
        name='account_income_transaction_new'),
    url(r'^(?P<account_id>\d+)/expenditure-transactions/new$', ExpenditureTransactionFormView.as_view(),
        name='account_expenditure_transaction_new'),
]


router = DefaultRouter()
router.register(r'api', AccountViewSet, base_name='account_api')
urlpatterns += router.urls
