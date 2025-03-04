from django.shortcuts import render
from .models import Employee, Course,Student, Department
from rest_framework.response import Response
from rest_framework.decorators import api_view,APIView
from .serializers import DepartmentSerializer, EmployeeSerializer
from rest_framework import generics



# Create your views here.
# Normal View
def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'model_relation/employee.html', {'employees':employees})



# API View function type
@api_view(['GET'])
def course_list(request):
    courses = Course.objects.all()
    return Response({'message':'I am testing API for function type views'})

#API Views Class type

class Students(APIView):
    def get(self, request):
        students = Student.objects.all()
        return Response({'message':'I am testing API for Class type views'})
    
# with serializer to help with query
class DepartmentListCreateAPIView(generics.ListCreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer