from django.contrib.auth import get_user_model
from django.test import TestCase

from rest_framework.test import APITestCase



class ContractualPartyTests(APITestCase):

    def setUp(self) -> None:
        body = {
            'username': 'blabber',
            'password': 'blabber',
            'email': 'a@g.com'
        }
        response = self.client.post("/api/v1/users/", data=body)
        self.assertEquals(response.status_code, 201)
        all_names = [user.username for user in get_user_model().objects.all()]
        self.assertTrue('blabber' in all_names)

    def test_create_contractual_party(self):
        legal_entity="APG"
        body = {'legal_entity': legal_entity}
        self.client.login(username='blabber', password='blabber')
        response = self.client.post("/api/v1/contractual_parties/", data=body)
        self.assertEquals(response.status_code, 201)