from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from students.models import Student
from .student_serializers import StudentSerializer


class StudentApiListView(APIView):
    def get(self, request):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)
    

class StudentDetailApiView(APIView):
    def get(self, request,id):
        student = get_object_or_404(Student,id=id)
        serializer = StudentSerializer(student)
        return Response(serializer.data)
    

class StudentUpdateApiView(APIView):
    def put(self, request,id):
        student = get_object_or_404(Student,id=id)
        rezult = request.data
        serializer = StudentSerializer(instance=student,data=rezult)

        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def patch(self, request,id):
        student = get_object_or_404(Student,id=id)
        rezult = request.data
        serializer = StudentSerializer(instance=student, data=rezult, partial=True)

        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    

class StudentCreateApiView(APIView):
    def post(self, request):
        rezult = request.data
        serializer = StudentSerializer(data=rezult)

        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    

