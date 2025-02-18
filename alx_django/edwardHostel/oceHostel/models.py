from django.db import models

# Create your models here.
class Hostels(models.Model):
    #hostel_id = models.IntegerField(null=False)
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=100)
    number_of_rooms = models.IntegerField(null=True)
    published_date = models.DateField(auto_now_add=True)
    date_modified = models.DateField(auto_now=True)
    
    def __str__(self):
        return f"{self.name} is available at {self.location}"

'''
#retrieving data
hostel = Hostels.objects.all()
#filter data
hostels_by_name = Hostels.objects.filter(name = 'OCE')
#order data
order_hostels_by_date = Hostels.objects.order_by('published_date')

#creating a new hostel
new_hostel = Hostels(name = 'Applerose New', number_of_rooms = 10, location = 'oce campus')
new_hostel.save()
'''