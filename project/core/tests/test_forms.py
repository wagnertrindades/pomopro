from django.test import TestCase 
from django.test.client import Client 
from django.core.urlresolvers import reverse

from project.core.models import User 

class LoginTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create(
            email='test@test.com', name='test', password='test'
        )

    def tearDown(self):
        self.user.delete()

    def test_login_form_error(self):
        data = {'email': 'test@test.com', 'password': ''}
        client = Client()
        path = reverse('core:home')
        response = client.post(path, data)
        self.assertFormError(response, 'form', 'password','Este campo é obrigatório.')

    def test_login_form_success(self):
        data = {'email': 'test@test.com', 'password': 'test'}
        client = Client()
        path = reverse('core:home')
        response = client.post(path, data)
        self.assertEqual(response.status_code, 200)

    def test_register_form_error(self):
        data = {'nome': 'tests', 'email': 'tests@tests.com', 'password1': '123', 'password2': 'ref'}
        client = Client()
        path = reverse('core:register')
        response = client.post(path, data)
        self.assertFormError(response, 'form', 'password2', 'A confirmação não está correta')

    def test_register_form_sucess(self):
        data = {'nome': 'tests', 'email': 'tests@tests.com', 'password1': '1234', 'password2': '1234'}
        client = Client()
        path = reverse('core:register')
        response = client.post(path, data)
        self.assertEqual(response.status_code, 200)
