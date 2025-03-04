from django.shortcuts import render
from .models import Employee, Course,Student, Department
from rest_framework.response import Response
from rest_framework.decorators import api_view,APIView
from .serializers import DepartmentSerializer, StudentSerializer, CourseSerializer
from rest_framework import generics
from rest_framework import status



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


@api_view(['POST'])
def create_student(request):
    serializer = StudentSerializer(data=request.data)  # Deserialize request data
    
    if serializer.is_valid():
        serializer.save()  # Save the validated data to the database
        return Response({'message': 'Student created successfully', 'data': serializer.data}, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#API Views Class type

class Students(APIView):
    def get(self, request):
        students = Student.objects.all()
        return Response({'message':'I am testing API for Class type views'})
    
# with serializer to help with query
class DepartmentListCreateAPIView(generics.ListCreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer