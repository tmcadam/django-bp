from django.contrib.auth.models import User
from django.test import TestCase, tag
from django.urls import reverse

class UrlTests(TestCase):

    def setUp(self):
        User.objects.create_superuser('myuser', 'myemail@test.com', 'mypassword')

    @tag("urls-tests")
    def  test_routing_admin_url(self):
        url = reverse('admin:index')
        self.client.login(username='myuser', password='mypassword')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)