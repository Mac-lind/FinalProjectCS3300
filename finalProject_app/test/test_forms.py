from django.test import TestCase
from finalProject_app.forms import PlantForm

class FormsTest(TestCase):
    def test_valid_plant_form(self):
        data = {'name': 'Test Plant', 'function': 'Test Function', 'location': 'Test Location'}
        form = PlantForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_plant_form(self):
        data = {'name': '', 'function': 'Test Function', 'location': 'Test Location'}
        form = PlantForm(data=data)
        self.assertFalse(form.is_valid())
