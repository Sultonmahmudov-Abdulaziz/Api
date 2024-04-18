from django.shortcuts import render
from django.views import View
from .models import Student



class StudentsListView(View):
    def get(self, request):
        students = Student.objects.all()

        data = {
            "students": students 
        }
        return render(request,'students/list.html',context=data)

