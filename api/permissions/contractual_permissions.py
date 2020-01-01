import logging

from django.db.models import Q
from rest_framework.permissions import BasePermission

from contracts.models import UserContractualPartyAssociation

logger = logging.getLogger(__name__)


class AdminForContractualPartyPermission(BasePermission):
    """
    Checks whether an association exists of type "Administrator" for the user in the context of
    the given company refered to by 'other_party'
    """
    message = "You are not an administrator of that contractual party."

    def has_permission(self, request, view):
        user = request.user
        other_party_id = request.data['other_party']
        assocs = UserContractualPartyAssociation.objects.filter(
            Q(user=user) & Q(cp_id=other_party_id) & Q(association_type='Administrator'))
        if assocs:
            return True
        else:
            logger.warning("Illegal Access: User is not an administrator of the given contractual party.")
            return False
