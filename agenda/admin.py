from django.contrib import admin
from .models import Event, Department

class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_beginning', 'organizer', 'city')
    list_filter = ('organizer', 'department')
    date_hierarchy = 'date_beginning'
    ordering       = ('date_beginning', )


admin.site.register(Event, EventAdmin)
admin.site.register(Department)