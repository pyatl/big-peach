from django.contrib import admin
from events.models import Location, Event


class EventAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ('name', 'start', 'location')


class LocationAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Location, LocationAdmin)
admin.site.register(Event, EventAdmin)
