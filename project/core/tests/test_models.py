from django.test import TestCase

from project.core.models import User

class UserTestCase(TestCase):

    def test_user_create(self):
        # Create
        user = User.objects.create(email='test@test.com', name='test', password='123')
        # Get All
        users = User.objects.all()
        # Assert
        self.assertEqual(users[0], user)
