from django.urls import path, include
from . import views


urlpatterns = [
#path function defines a url pattern
#'' is empty to represent based path to app
# views.index is the function defined in views.py
# name='index' parameter is to dynamically create url
# example in html <a href="{% url 'index' %}">Home</a>.
path('', views.index, name='index'),
path('accounts/', include('django.contrib.auth.urls')),
path('plants/', views.PlantListView.as_view(), name='plants'),
path('plants/<int:pk>', views.PlantDetailView.as_view(), name='plant-detail'),
path('work/', views.WorkOrdersListView.as_view(), name='work'),
path('work/<int:pk>', views.WorkOrdersDetailView.as_view(), name='work-detail'),
path('employees/', views.EmployeeListView.as_view(), name='employees'),
path('employees/<int:pk>/', views.EmployeeDetailView.as_view(), name='employee-detail'),

path('plants/create/', views.PlantCreateView.as_view(), name='plant-create'),
path('plants/edit/<int:pk>/', views.PlantEditView.as_view(), name='plant-edit'),
path('plants/delete/<int:pk>/', views.PlantDeleteView.as_view(), name='plant-delete'),
path('work/create/', views.WorkCreateView.as_view(), name='work-create'),
path('work/edit/<int:pk>/', views.WorkEditView.as_view(), name='work-edit'),
path('work/delete/<int:pk>/', views.WorkDeleteView.as_view(), name='work-delete'),
path('employees/create/', views.EmployeeCreateView.as_view(), name='employee-create'),
path('employees/edit/<int:pk>/', views.EmployeeEditView.as_view(), name='employee-edit'),
path('employees/delete/<int:pk>/', views.EmployeeDeleteView.as_view(), name='employee-delete'),

path('user/', views.userPage, name='user_page'),
path('login/', views.loginPage, name='login'),
path('accounts/register/', views.registerPage, name='register_page'),
]
