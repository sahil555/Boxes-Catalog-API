from django.db import models

# Create your models here.

from django.urls import reverse  # To generate URLS by reversing URL patterns
import uuid 
from datetime import date

from django.contrib.auth.models import User


class Box(models.Model):
    name = models.CharField(max_length=100)
    length = models.IntegerField(default=0)
    width = models.IntegerField(default=0)
    height = models.IntegerField(default=0)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    # Foreign Key used because box can only have one author, but authors can have multiple boxes
    # Author as a string rather than object because it hasn't been declared yet in file.
    
    def get_absolute_url(self):
        """Returns the url to access a particular book instance."""
        return reverse('Box-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return (self.length,self.width,self.height,self.area,self.volume)


class Author(models.Model):
    """Model representing an author."""
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    

    def get_absolute_url(self):
        """Returns the url to access a particular author instance."""
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return '{0}, {1}'.format(self.name, self.date_of_birth)
