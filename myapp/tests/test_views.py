from .test_setup import TestSetup


class TestViews(TestSetup):

    def test_user_cannot_register_without_data(self):
        res = self.client.post(self.register_url)

        self.assertEqual(res.status_code, 400)

    def test_user_can_register_with_data(self):
        res = self.client.post(self.register_url, self.user_data, format="json")
        self.assertEqual(res.data['username'], self.user_data['username'])
        
        self.assertEqual(res.status_code, 201)

    def test_user_cannot_login_with_null_data(self):
        self.client.post(self.register_url, self.user_data, format="json")
        data = {
            "username": "",
            "password": ""
        }
        res = self.client.post(self.login_url, data, format = "json")
        
        self.assertEqual(res.status_code, 400)


    def test_user_cannot_login_with_invalid_data(self):
        self.client.post(self.register_url, self.user_data, format="json")
        data = {
            "username": self.user_data["username"],
            "password": "wrongpassword"
        }
        res = self.client.post(self.login_url, data, format = "json")
        
        self.assertEqual(res.status_code, 401)


    def test_user_can_login_with_valid_data(self):
        self.client.post(self.register_url, self.user_data, format="json")
        data = {
            "username": self.user_data["username"],
            "password": self.user_data["password"]
        }
        res = self.client.post(self.login_url, data, format = "json")
        
        self.assertTrue(res.data['access'])
        self.assertTrue(res.data['refresh'])
        self.assertEqual(res.status_code, 200) 


    def test_user_can_perform_partial_or_full_information_update(self):
        self.client.post(self.register_url, self.user_data, format="json")
        data = {
            "username": self.user_data["username"],
            "password": self.user_data["password"]
        }
        res_login = self.client.post(self.login_url, data, format = "json")
        
        self.assertTrue(res_login.data['access'])
        self.assertTrue(res_login.data['refresh'])

        self.client.credentials(
            HTTP_AUTHORIZATION='Bearer ' + res_login.data['access'])
        partial_data = {
            "username": 'winner',
            "first_name": 'james'
        }

        res_update = self.client.patch(self.user_url, partial_data, format = "json")
        self.assertEqual(res_update.status_code, 200)


    def test_user_cannot_add_order_without_authentication(self):
        
        res_create_orders = self.client.post(self.order_url, self.order_data, format = "json")
        self.assertEqual(res_create_orders.status_code, 401)

       
                                   

    def test_user_can_add_order_while_authenticated(self):
        self.client.post(self.register_url, self.user_data, format="json")
        data = {
            "username": self.user_data["username"],
            "password": self.user_data["password"]
        }
        res_login = self.client.post(self.login_url, data, format = "json")
        
        self.assertTrue(res_login.data['access'])
        self.assertTrue(res_login.data['refresh'])

        self.client.credentials(
            HTTP_AUTHORIZATION='Bearer ' + res_login.data['access'])    
        res_create_orders = self.client.post(self.order_url, self.order_data, format = "json")

        self.assertEqual(res_create_orders.status_code, 201)

        # self.assertEqual(res.status_code, 200)                                 


    def test_user_cannot_view_order_history_while_unauthenticated(self):
        res = self.client.get(self.order_url, format = "json")
        self.assertEqual(res.status_code, 401)


    def test_user_can_view_order_history_while_authenticated(self):
        self.client.post(self.register_url, self.user_data, format="json")
        data = {
            "username": self.user_data["username"],
            "password": self.user_data["password"]
        }
        res_login = self.client.post(self.login_url, data, format = "json")
        
        self.assertTrue(res_login.data['access'])
        self.assertTrue(res_login.data['refresh'])

        self.client.credentials(
            HTTP_AUTHORIZATION='Bearer ' + res_login.data['access'])   

        res_create_orders = self.client.post(self.order_url, self.order_data, format = "json")
        self.assertEqual(res_create_orders.status_code, 201)

        res_orders = self.client.get(self.order_url, format = "json")
        self.assertTrue(res_orders.data)
        self.assertEqual(res_orders.status_code, 200)

                                       
    