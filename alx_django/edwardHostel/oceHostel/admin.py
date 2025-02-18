from django.contrib import admin
from .models import Hostels
# Register your models here.
class HostelAdmin(admin.ModelAdmin):
    list_display = ("name", "location", "number_of_rooms")
    search_fields = ("name", "location")
    dbjdbjs = ("name")
admin.site.register(Hostels, HostelAdmin)
