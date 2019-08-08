from django.db import models
from urllib.parse import quote

# Create your models here.

class Event(models.Model):
    title = models.CharField(max_length=100, verbose_name = "titre")
    organizer = models.CharField(max_length=42, verbose_name = "organisateur")
    date_beginning = models.DateField(verbose_name="date de début")
    date_end = models.DateField(null=True, verbose_name = "date de fin")
    location = models.CharField(max_length=100, verbose_name = "nom du lieu")
    address = models.CharField(max_length=100, verbose_name = "adresse")
    zipcode = models.IntegerField(verbose_name = "code postal")
    city = models.CharField(max_length=100, verbose_name = "ville")
    department = models.ForeignKey('Department', on_delete=models.SET_NULL, null=True, verbose_name="département")
    description = models.TextField()

    class Meta:
        verbose_name = "événement"
        ordering = ['date_beginning']
        
    def __str__(self):
        return self.title

    def get_url_maps(self):
        url = "https://maps.google.com/maps?q="
        end = "&t=&z=13&ie=UTF8&iwloc=&output=embed"
        url += quote(self.location, safe="") + quote(" ", safe="") + quote(self.address, safe="") + quote(" ", safe="") + quote(self.city, safe="") + end
        return url

class Department(models.Model):
    name = models.CharField(max_length=30)
    number = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "département"
        ordering = ['name']