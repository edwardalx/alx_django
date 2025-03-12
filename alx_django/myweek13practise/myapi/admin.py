from django.contrib import admin

from .models import Customer, Player

# Register your models here.
admin.site.register([Player,Customer])