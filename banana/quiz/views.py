from .models import InterestQuiz
from .serializers import InterestQuizSerializer
from rest_framework import generics


class InterestQuizListCreate(generics.ListCreateAPIView):
    queryset = InterestQuiz.objects.all()
    serializer_class = InterestQuizSerializer
