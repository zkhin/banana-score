from django.db import models


class InterestQuiz(models.Model):
    topic = models.CharField(max_length=100)
    trend_word = models.CharField(max_length=50)
    banana_score = models.IntegerField()
    trend_score = models.IntegerField()
    date_created = models.DateTimeField('date created')


class UserQuiz(models.Model):
    quiz = models.ForeignKey(InterestQuiz, on_delete=models.CASCADE)
