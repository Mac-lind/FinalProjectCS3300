from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Plants(models.Model):
#List of choices for major value in database, human readable name

    name = models.CharField(max_length=200, blank=False)
    function = models.CharField(max_length=200, blank=False)
    location = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('plant-detail',args=[str(self.id)])
    def get_workorders(self):
        # Retrieve the related work orders for this plant
        return WorkOrders.objects.filter(plant=self)
    
class WorkOrders(models.Model):
#List of choices for major value in database, human readable name

    name = models.CharField(max_length=200, blank=False)
    plant = models.ForeignKey(Plants, on_delete=models.CASCADE, default=None)
    description = models.CharField(max_length=200, blank=False)
    priority = models.CharField(max_length=200, blank=True)
    startDate = models.DateField(blank=True, null=True)
    endDate = models.DateField(blank=True, null=True)
 
    
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('work-detail',args=[str(self.id)])
    
class Employee(models.Model):
#List of choices for major value in database, human readable name

    name = models.CharField(max_length=200, blank=False)
    workTitle = models.CharField(max_length=200, blank=False)
    email = models.CharField(max_length=200, blank=True)
    workOrder = models.OneToOneField(WorkOrders, null=True, on_delete=models.CASCADE, unique=True)
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('employee-detail',args=[str(self.id)])
    