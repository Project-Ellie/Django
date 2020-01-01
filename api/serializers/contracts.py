from rest_framework import serializers
from contracts.models import ContractualParty, Contract


class ContractualPartyApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContractualParty
        fields = ('legal_entity', 'id')


class ContractApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = ('id', 'other_party', 'other_party_role', 'start_date')
