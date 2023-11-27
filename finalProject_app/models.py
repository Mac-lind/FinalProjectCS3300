from django.db import models


# Create your models here.


class Plants(models.Model):


#List of choices for major value in database, human readable name

    name = models.CharField(max_length=200, blank=False)
    function = models.CharField(max_length=200, blank=False)
    
