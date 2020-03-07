from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Question(models.Model):
    text = models.TextField()
    u_date = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return self.text


class Answer(models.Model):
    text = models.TextField()
    is_true = models.BooleanField(default=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return self.text