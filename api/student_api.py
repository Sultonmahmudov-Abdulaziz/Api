from rest_framework.views import APIView
from rest_framework.response import Response
from students.models import Student
from .student_serializers import StudentSerializer


class StudentApiListView(APIView):
    def get(self, request):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)