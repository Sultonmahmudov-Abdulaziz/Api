from django.urls import path
from .views import StudentsListView


app_name = "students"

urlpatterns = [
    path('list/', StudentsListView.as_view(), name='list'),
]