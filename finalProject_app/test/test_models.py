from django.test import TestCase
from finalProject_app.models import Plants, WorkOrders, Employee
from django.contrib.auth.models import User

class ModelsTest(TestCase):
    def test_plant_creation(self):
        plant = Plants.objects.create(name='Test Plant', function='Test Function', location='Test Location')
        self.assertEqual(plant.name, 'Test Plant')

    def test_work_order_creation(self):
        plant = Plants.objects.create(name='Test Plant', function='Test Function', location='Test Location')
        work_order = WorkOrders.objects.create(name='Test Work Order', plant=plant, description='Test Description')
        self.assertEqual(work_order.name, 'Test Work Order')

    def test_employee_creation(self):
        user = User.objects.create(username='testuser')
        plant = Plants.objects.create(name='Test Plant', function='Test Function', location='Test Location')
        work_order = WorkOrders.objects.create(name='Test Work Order', plant=plant, description='Test Description')
        employee = Employee.objects.create(name='Test Employee', workTitle='Test Title', email='test@example.com', user=user, workOrder=work_order)
        self.assertEqual(employee.name, 'Test Employee')
