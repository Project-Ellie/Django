from django.test import TestCase
import logging

from users.models import CustomUser
from .models import ContractualParty, Contract, UserContractualPartyAssociation

logger = logging.getLogger(__name__)


class Explorations(TestCase):

    def setUp(self):
        logger.info("setting up the test case")
        admin = CustomUser(username="Admin", password="admin")
        admin.save()
        apg = ContractualParty(legal_entity="APG/SGA", created_by=admin)
        apg.save()
        self.apg = apg
        c1_apg = Contract(other_party=apg, other_party_role=Contract.AGENCY)
        c2_apg = Contract(other_party=apg, other_party_role=Contract.SITE_OWNER)
        c1_apg.save()
        c2_apg.save()
        self.contracts = [c1_apg, c2_apg]

    def test_sth(self):
        apg = ContractualParty.objects.all()[0]
        self.assertEquals(apg, self.apg)
        self.assertEquals(apg.contract_set.all().count(), 2)
        wolfie = CustomUser(username="Wolfie", password="blubber")
        wolfie.save()
        w_apg = UserContractualPartyAssociation(cp=apg, user=wolfie)
        w_apg.save()
