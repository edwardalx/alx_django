from django.shortcuts import render
from .models import Employee, Course,Student, Department
from rest_framework.response import Response
from rest_framework.decorators import api_view,APIView
from .serializers import DepartmentSerializer, MyModelSerializer, StudentSerializer, CourseSerializer
from rest_framework import generics 
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.permissions import BasePermission



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


#Authorisation
class EdwardView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({'message':'I am testing API for Class type views'})


'''Permission - Customed to allows read-only access to everyone,
 but requires the user to be an admin (staff user) for any write operations.'''


class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True
        return request.user.is_staff
    
class MyModelListView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Only authenticated users can view the list of models
        queryset = Department.objects.all()
        serializer = MyModelSerializer(queryset, many=True)
        return Response(serializer.data)

class MyModelCreateView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]

    def post(self, request):
        # Only admin users can create new model instances
        serializer = MyModelSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)