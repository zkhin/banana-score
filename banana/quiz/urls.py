from django.urls import path
from . import views

urlpatterns = [
    path('api/interestquiz/', views.InterestQuizListCreate.as_view()),
]
