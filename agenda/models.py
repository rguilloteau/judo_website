from django.db import models

# Create your models here.

class Event(models.Model):
    title = models.CharField(max_length=100, verbose_name = "titre")
    organizer = models.CharField(max_length=42, verbose_name = "organisateur")
    date_beginning = models.DateTimeField(verbose_name="date de début")
    date_end = models.DateTimeField(null=True, verbose_name = "date de fin")
    location = models.CharField(max_length=100, verbose_name = "nom du lieu")
    address = models.CharField(max_length=100, verbose_name = "adresse")
    city = models.CharField(max_length=100, verbose_name = "ville")
    department = models.ForeignKey('Department', on_delete=models.SET_NULL, null=True, verbose_name="département")
    description = models.TextField()

    class Meta:
        verbose_name = "événement"
        ordering = ['date_beginning']
        
    def __str__(self):
        return self.title

class Department(models.Model):
    name = models.CharField(max_length=30)
    number = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "département"
        ordering = ['name']