from django.contrib import admin
from .models import Contract, ContractualParty, UserContractualPartyAssociation


admin.site.register(Contract)
admin.site.register(ContractualParty)
admin.site.register(UserContractualPartyAssociation)
# Register your models here.
