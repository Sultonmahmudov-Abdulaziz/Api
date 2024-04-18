from django.urls import path
from .views import CardApiView,OneCardApiView
from .student_api import StudentApiListView



urlpatterns = [
    path('cards/', CardApiView.as_view(), name='cards'),
    path('one-card/', OneCardApiView.as_view(), name='one_card'),
    path('create-card/', CardApiView.as_view(), name='create_card'),
    path('student-api/', StudentApiListView.as_view(), name='student_api'),

]