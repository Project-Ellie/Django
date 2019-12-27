from rest_framework import serializers
from contracts.models import ContractualParty


class ContractualPartyApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContractualParty
        fields = ('legal_entity', 'created_by')
