from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.http import HttpResponse

from app.models import Question, Answer

User = get_user_model()


def home(request):
    return render(request, "home.html")

def racing(request):
    
    question_text=Question.objects.all()
    answers=Answer.objects.all()

    context={
        "question_text":question_text,
        "answers":answers
    }

    return render(request, "racing.html", context)

def result(request):
    return render(request, "result.html")

def about(request):
    return render(request, "about.html")