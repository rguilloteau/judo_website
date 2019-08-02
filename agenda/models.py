from django.db import models

# Create your models here.

class event(models.Model):
    title = models.CharField(max_length=100)
    organizer = models.CharField(max_length=42)
    date_beginning = models.DateTimeField()
    date_end = models.DateTimeField(null=True)
    department = models.ForeignKey('Department', on_delete=models.SET_NULL, null=True)
    location = models.CharField(max_length=100)
    description = models.TextField()

    class Meta:
        ordering = ['date_beginning']
        
    def __str__(self):
        return self.title

class Department(models.Model):
    name = models.CharField(max_length=30)
    number = models.IntegerField()

    def __str__(self):
        return self.name