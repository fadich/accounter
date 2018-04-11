from rest_framework.viewsets import ModelViewSet
from website.api.serializer import AccountSerializer
from website.models import Account


class AccountViewSet(ModelViewSet):
    serializer_class = AccountSerializer
    queryset = Account.objects.all()
