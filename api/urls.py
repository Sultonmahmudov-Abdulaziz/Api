from django.urls import path
from .views import CardApiView,OneCardApiView
from .student_api import StudentApiListView,StudentDetailApiView,StudentUpdateApiView



urlpatterns = [
    path('cards/', CardApiView.as_view(), name='cards'),
    path('one-card/', OneCardApiView.as_view(), name='one_card'),
    path('create-card/', CardApiView.as_view(), name='create_card'),

    # student api views

    path('student-api/', StudentApiListView.as_view(), name='student_api'),
    path('student-detail/<int:id>/', StudentDetailApiView.as_view(), name='student_detail'),
    path('student-update/<int:id>/', StudentUpdateApiView.as_view(), name='student_update'),

]