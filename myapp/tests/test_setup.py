import imp
from rest_framework.test import APITestCase
from django.urls import reverse


class TestSetup(APITestCase):

    def setUp(self):
        self.register_url = reverse('register')
        self.login_url = reverse('token_obtain_pair')
        self.order_url = reverse('orders')
        self.user_url = reverse('user')

        self.user_data = {
            'username':'peter',
            'email': 'peter@gmail.com',
            'password': 'youg22@@',
            'first_name': 'peter',
            'last_name': 'james'
        }
        self.order_data = {
            'user': 1,
            'transaction_id': 'randomrandoom@@',
            'total': 2000
        }
        return super().setUp()

    def tearDown(self):
        return super().tearDown()     
    
