from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.http import HttpResponse

from app.models import Question, Answer

User = get_user_model()


def home(request):
    return render(request, "home.html")


def testing(request):
    questions = Question.objects.all()
    answers = Answer.objects.all()

    context = {
        "questions": questions,
        "answers": answers
    }

    if request.method == "POST":
        true_answers = 0
        false_answers = 0
        for question in questions:
            for answer in answers:
                if answer.question.id == question.id:
                    key = "answers"
                    key = key + str(question.id)
                    user_answer = request.POST.get(key)
                    if answer.text == user_answer:
                        correct_answer = Answer.objects.get(
                            question=question, is_true=True)
                        if user_answer == correct_answer.text:
                            true_answers = true_answers + 1
                        else:
                            false_answers = false_answers + 1

        context["result"] = {
            "true_answers": true_answers,
            "false_answers": false_answers
        }

    return render(request, "testing.html", context)


def about(request):
    return render(request, "about.html")
