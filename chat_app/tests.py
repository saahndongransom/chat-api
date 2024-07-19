from django.test import TestCase

import json
from django.test import TestCase
import requests

class ChatEndpointTestCase(TestCase):
    base_url = 'http://127.0.0.1:8000' 

    def test_chat_list_endpoint(self):
        response = requests.get(f'{self.base_url}/chats/')
        self.assertEqual(response.status_code, 200)

    def test_group_list_endpoint(self):
        response = requests.get(f'{self.base_url}/groups/')
        self.assertEqual(response.status_code, 200)

  

    def test_create_group_endpoint(self):
        data = {'name': 'Test Group', 'members': [1, 2]}  
        headers = {'Content-Type': 'application/json'}
        response = requests.post(f'{self.base_url}/groups/', headers=headers, data=json.dumps(data))
        self.assertEqual(response.status_code, 201)  

    

