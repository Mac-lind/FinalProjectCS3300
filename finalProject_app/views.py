from django.shortcuts import render, redirect
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from finalProject_app.forms import PlantForm, WorkOrderForm, EmployeeForm, CreateUserForm
from finalProject_app.models import Plants, WorkOrders, Employee
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import Group
from .decorator import allowed_users
from django.contrib import messages
from django.contrib.auth.views import LoginView


class PlantListView(generic.ListView):
    model = Plants


class PlantDetailView(generic.DetailView):
    model = Plants


class WorkOrdersDetailView(generic.DetailView):
    model = WorkOrders


class WorkOrdersListView(LoginRequiredMixin, generic.ListView):
    model = WorkOrders


class EmployeeDetailView(LoginRequiredMixin, generic.DetailView):
    model = Employee


class EmployeeListView(LoginRequiredMixin, generic.ListView):
    model = Employee


class PlantCreateView(CreateView):
    model = Plants
    form_class = PlantForm
    template_name = 'finalProject_app/plant_form.html'
    success_url = '/plants/'  # Redirect to the plant list after successful creation


class PlantEditView(UpdateView):
    model = Plants
    form_class = PlantForm
    template_name = 'finalProject_app/plant_edit.html'
    success_url = reverse_lazy('plants')  # Redirect to the plant list after successful edit


class PlantDeleteView(DeleteView):
    model = Plants
    template_name = 'finalProject_app/plant_delete.html'
    success_url = reverse_lazy('plants')  # Redirect to the plant list after successful deletion


class WorkCreateView(CreateView):
    model = WorkOrders
    form_class = WorkOrderForm
    template_name = 'finalProject_app/work_form.html'
    success_url = '/work/'  # Redirect to the plant list after successful creation


class WorkEditView(UpdateView):
    model = WorkOrders
    form_class = WorkOrderForm
    template_name = 'finalProject_app/work_edit.html'
    success_url = reverse_lazy('work')  # Redirect to the plant list after successful edit


class WorkDeleteView(DeleteView):
    model = WorkOrders
    template_name = 'finalProject_app/work_delete.html'
    success_url = reverse_lazy('work')  # Redirect to the plant list after successful deletion


class EmployeeCreateView(CreateView):
    model = Employee
    form_class = EmployeeForm
    template_name = 'finalProject_app/employee_form.html'
    success_url = '/employees/'


class EmployeeEditView(UpdateView):
    model = Employee
    form_class = EmployeeForm
    template_name = 'finalProject_app/employee_edit.html'
    success_url = reverse_lazy('employees')


class EmployeeDeleteView(DeleteView):
    model = Employee
    template_name = 'finalProject_app/employee_delete.html'
    success_url = reverse_lazy('employees')

def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            group = Group.objects.get(name='employee_role')
            user.groups.add(group)
            employee = Employee.objects.create(user=user,)
            workOrder = WorkOrders.objects.create()
            employee.workOrder = workOrder
            employee.save()

            messages.success(request, 'Account was created for ' + username)
            return redirect('login')
    context={'form':form}
    return render(request, 'registration/register.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles = ['employee_role'])
def createProject(request, plant_id):
    form = WorkOrderForm()
    plant = Plants.objects.get(pk=plant_id)
    if request.method == 'POST':
        workOrder_data = request.POST.copy()
        workOrder_data['plant_id'] = plant_id
        form = WorkOrderForm(workOrder_data)
        if form.is_valid():
            workOrder = form.save(comit=False)
            workOrder.plant = plant
            workOrder.save()

            return redirect('plant-detail', pk=plant_id)
    context = {'form':form}
    return render(request, 'finalProject_app/work_form.html')

@login_required(login_url='login')
@allowed_users(allowed_roles=['employee'])
def userPage(request):
    employee = request.user.employee
    form = EmployeeForm(instance = employee)
    print('employee', employee)
    workOrder = employee.work
    print(workOrder)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES, isinstance=employee)
        if form.is_valid():
            form.save()
    context = {'workOrder':workOrder, 'form':form}
    return render(request, 'finalProject_app/user.html', context)

def loginPage(request):
    return LoginView.as_view(template_name='finalProject_app/templates/registration/login.html')(request)

def index(request):
    # Render index.html
    return render(request, 'finalProject_app/index.html')
