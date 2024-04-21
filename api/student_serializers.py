from rest_framework import serializers
from students.models import Student


class StudentSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    class Meta:
        model = Student
        fields = ('id', 'frist_name', 'last_name', 'email')