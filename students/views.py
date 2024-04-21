from django.shortcuts import render,get_object_or_404,redirect
from django.views import View
from .models import Student
from .forms import StudentForm


class StudentsListView(View):
    def get(self, request):
        students = Student.objects.all()

        data = {
            "students": students 
        }
        return render(request,'students/list.html',context=data)
    

class StudentDetailView(View):
    def get(self, request,id):
        student = get_object_or_404(Student,id=id)
        form = StudentForm(instance=student)
        data = {
            "form": form ,
            "student": student
        }

        return render(request,'students/detail.html',context=data)


class StudentUpdateView(View):
    def post(self, request,id):
        student = get_object_or_404(Student,id=id)

        form = StudentForm(request.POST,instance=student)
        if form.is_valid():
            form.save()
            return redirect('students:list')
        

        return render(request,'students/detail.html', context={"form":form})


