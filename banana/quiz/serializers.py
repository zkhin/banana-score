from rest_framework import serializers
from quiz.models import InterestQuiz

class InterestQuizSerializer(serializers.ModelSerializer):
  class Meta:
    model = InterestQuiz
    fields = ('id', 'trend_word', 'banana_score', 'trend_score', 'date_created')