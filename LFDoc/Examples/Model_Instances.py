# MODEL INSTANCES (MODEL API)

from django.db import models
from django.forms import ValidationError

class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    
    # You can add method to the models like this
    @classmethod
    def create(cls, name):
        restaurant = cls(name = name)
        return restaurant
    
    
# This is the preffered way to add methods to a model
class SchoolManager(models.Manager):
    def create_school(self, name):
        school = self.create(name = name)
        return school

class School(models.Model):
    name = models.CharField(max_length=100)

    # you can use the school manager like so,
    objects = SchoolManager()


