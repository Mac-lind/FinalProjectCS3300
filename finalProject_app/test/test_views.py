from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from finalProject_app.models import Plants

class ViewsTest(TestCase):
    def test_plant_list_view(self):
        response = self.client.get(reverse('plants'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'finalProject_app/plants_list.html')
