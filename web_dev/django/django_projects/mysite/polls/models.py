from django.db import models
from django.utils import timezone
import datetime


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


class IMB_PingPong(models.Model):
    date = models.DateTimeField("date created")
    byte = models.IntegerField(default=0)
    repetitions = models.IntegerField(default=0)
    runtime = models.FloatField()
    mb_per_sec = models.FloatField()


class IMB_Bidir_Get(models.Model):
    date = models.DateTimeField("date created")
    byte = models.IntegerField(default=0)
    repetitions = models.IntegerField(default=0)
    runtime = models.FloatField()
    mb_per_sec = models.FloatField()
    mode = models.CharField(max_length=50)

    def __str__(self):
        return self.mode


class Benchmark_Threshold(models.Model):
    benchmark_name = models.CharField(max_length=256)
    threshold = models.FloatField(default=-1)

    def __str__(self):
        return self.mode
