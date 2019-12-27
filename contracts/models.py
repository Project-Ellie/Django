from django.db import models
from django.utils import timezone

from users.models import CustomUser


class ContractualParty(models.Model):
    """
    A legal entity (company or legal person) with a contract
    """
    legal_entity = models.CharField(max_length=256)


class Contract(models.Model):
    """
    contractual parameters defining the relationship to this company
    """
    SITE_OWNER = 'Site Owner'
    AGENCY = 'Agency'
    CREATIVE = 'Creative'
    PUBLISHER = 'Publisher'

    OP_ROLE_CHOICES = (
        (SITE_OWNER, 'Site Owner'),
        (AGENCY, 'Agency'),
        (CREATIVE, 'Creative Designer'),
        (PUBLISHER, 'Publisher')
    )

    other_party_role = models.CharField(choices=OP_ROLE_CHOICES, max_length=128)
    other_party = models.ForeignKey(ContractualParty,
                                    on_delete=models.PROTECT,)
    start_date = models.DateTimeField(default=timezone.now)


class ContractualPartyAssociation(models.Model):
    """
    Association of a CustomUser with the ContractualParty
    """
    user = models.ForeignKey(CustomUser, on_delete=models.PROTECT)
    cp = models.ForeignKey(ContractualParty, on_delete=models.PROTECT)
    valid_from = models.DateTimeField(default=timezone.now)
    valid_to = models.DateTimeField(null=True)
