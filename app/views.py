from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model

from app.models import Question, Answer

User = get_user_model()


def home(request):
    return render(request,"home.html")

def racing(request):
    return render(request,"racing.html")

def about(request):
    return render(request,"about.html")