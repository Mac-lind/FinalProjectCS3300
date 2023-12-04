# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Plants, WorkOrders, Employee

class PlantForm(forms.ModelForm):
    class Meta:
        model = Plants
        fields = ['name', 'function', 'location']

class WorkOrderForm(forms.ModelForm):
    class Meta:
        model = WorkOrders
        fields = ['name', 'plant', 'description', 'priority', 'startDate', 'endDate']

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'workTitle', 'email', 'workOrder']
        exclude =['user', 'workOrder']
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
