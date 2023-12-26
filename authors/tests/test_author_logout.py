from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse


class AuthorLogout(TestCase):
    def test_user_tries_to_logout_using_get_method(self):
        User.objects.create_user(username='my_user', password='my_pass')
        self.client.login(username='my_user', password='my_pass')

        url = reverse('authors:logout')
        response = self.client.get(url, follow=True)

        self.assertIn('Invalid logout request',
                      response.content.decode('utf-8'))

    def test_user_tries_to_logout_another_user(self):
        User.objects.create_user(username='my_user', password='my_pass')
        self.client.login(username='my_user', password='my_pass')

        url = reverse('authors:logout')
        response = self.client.post(
            url,
            data={
                'username': 'another_user'
            },
            follow=True
        )

        self.assertIn('Invalid logout user',
                      response.content.decode('utf-8'))

    def test_user_can_logout_successfully(self):
        User.objects.create_user(username='my_user', password='my_pass')
        self.client.login(username='my_user', password='my_pass')

        url = reverse('authors:logout')
        response = self.client.post(
            url,
            data={
                'username': 'my_user'
            },
            follow=True
        )

        self.assertIn('Logged out successfully',
                      response.content.decode('utf-8'))
