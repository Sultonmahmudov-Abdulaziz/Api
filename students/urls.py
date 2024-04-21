from django.urls import path
from .views import StudentsListView,StudentDetailView,StudentUpdateView


app_name = "students"

urlpatterns = [
    path('list/', StudentsListView.as_view(), name='list'),
    path('detail/<int:id>/', StudentDetailView.as_view(), name='detail'),
    path('update/<int:id>/', StudentUpdateView.as_view(), name='update'),
]