from django.db import models

class Student(models.Model):
    frist_name = models.CharField(max_length=125)
    last_name = models.CharField(max_length=125)
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"{self.frist_name} {self.last_name}"