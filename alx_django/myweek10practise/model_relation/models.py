from django.db import models
from django.contrib.auth.models import User

# Create your models here.
'''
mySql would be:
Create Table IF NOT EXIST Company(
Company_id INT PRIMARY KEY UNIQUE AUTO_INCREMENT,
department VARCHAR(100) Null,
employees VARCHAR(100) Null ,
FOREIGN KEY(employees) REFERENCES User(id)
)
'''
# class Company(models.Model):
#     department = models.CharField(max_length=100, null=True)
#     employees = models.ForeignKey(User, on_delete=models.CASCADE)

class Employees(models.Model):
    name = models.CharField(max_length=250, null= False)

class Department(models.Model):
    name = models.CharField(max_length=255, null = True)
    employee = models.ForeignKey(Employees, on_delete=models.CASCADE)

class Products(models.Model):
    product_name = models.CharField(max_length=255, null = False, unique=True)
class ProductDetail(models.Model):
    product = models.OneToOneField(Products, on_delete=models.CASCADE)
    detailed_discription = models.CharField(max_length=255)

class Students(models.Model):
    name = models.CharField(max_length=255, null=False)
    course = models.CharField(max_length=255, null=False)

class Courses(models.Model):
    course_title = models.CharField(max_length=255, null=False)
    sudents = models.ManyToManyField(Students, on_delete=models.CASCADE)


