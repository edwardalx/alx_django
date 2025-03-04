from django.urls import path
from .views import employee_list, course_list, Students

urlpatterns = [
    path('', view=employee_list, name='employees'),
    path('courses/', view=course_list, name='courses'),
    path('student/', view=Students.as_view(), name='students'),
]
