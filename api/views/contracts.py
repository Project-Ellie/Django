from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
import logging

from contracts.models import ContractualParty, Contract, UserContractualPartyAssociation
from ..permissions.contractual_permissions import AdminForContractualPartyPermission
from ..serializers import ContractualPartyApiSerializer, ContractApiSerializer

logger = logging.getLogger(__name__)


class ContractualPartyApiView(generics.ListCreateAPIView):

    permission_classes = [IsAuthenticated]
    queryset = ContractualParty.objects.all()
    serializer_class = ContractualPartyApiSerializer

    def create(self, request, *args, **kwargs):

        # TODO: It works but is this really the way to go? I don't think so!!
        # It circumvents a lot of checks in the serializer's save() method. However, it's unclear to me
        # How to set the created_by field to satisfy the procedure, since it uses validated_data to create
        # the model instance but I seem to be unable to populate it correctly.
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        cp = ContractualParty(created_by=request.user, legal_entity=request.data['legal_entity'])
        cp.save()
        response = request.data.copy()
        response['id'] = cp.id
        assoc = UserContractualPartyAssociation(
            user=request.user, cp=cp,
            association_type=UserContractualPartyAssociation.TYPE_ADMINISTRATOR)
        assoc.save()

        headers = self.get_success_headers(serializer.data)
        return Response(response, status=status.HTTP_201_CREATED, headers=headers)


class ContractApiView(generics.ListCreateAPIView):

    permission_classes = [IsAuthenticated, AdminForContractualPartyPermission]
    queryset = Contract.objects.all()
    serializer_class = ContractApiSerializer

    def create(self, request, *args, **kwargs):
        """
        A user can create a contract for a ContractualParty, she is administrator of.
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        contract = Contract(**serializer.validated_data)
        contract.save()
        response = request.data.copy()
        response['id'] = contract.id

        headers = self.get_success_headers(serializer.data)
        return Response(response, status=status.HTTP_201_CREATED, headers=headers)
