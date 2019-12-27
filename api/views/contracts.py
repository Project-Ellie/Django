from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from contracts.models import ContractualParty
from ..serializers import ContractualPartyApiSerializer


class ContractualPartyApiView(generics.ListCreateAPIView):

    permission_classes = [IsAuthenticated]
    queryset = ContractualParty.objects.all()
    serializer_class = ContractualPartyApiSerializer

    def create(self, request, *args, **kwargs):
        print(request.user)
        self.get_object().created_by = request.user
        return super(ContractualPartyApiView, self).create(request, *args, **kwargs)
