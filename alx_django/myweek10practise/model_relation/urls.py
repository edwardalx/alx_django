from django.urls import path
from .views import employee_list, course_list,create_student, Students, DepartmentListCreateAPIView

urlpatterns = [
    path('', view=employee_list, name='employees'),
    path('courses/', view=course_list, name='courses'),
    path('students/', view=Students.as_view(), name='students'),
    path('api/departments', view=DepartmentListCreateAPIView .as_view(), name='departments'),
    path('api/createstudent/', view=create_student, name='create_student'),
]
