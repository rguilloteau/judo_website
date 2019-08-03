from django.shortcuts import render, get_object_or_404
from agenda.models import Event

# Create your views here.

def home(request):
    events = Event.objects.all() #Event list
    return render(request, 'agenda/home.html', {'events' : events})

def read(request, id):
    event = get_object_or_404(Event, id=id)
    return render(request, 'agenda/read.html', {'event':event})