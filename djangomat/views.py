from django.shortcuts import render
from django.http import HttpResponse
from dataentry.tasks import celery_test_task

def home(request):
    return render(request, "home.html", {})


def celery_test(request):
    msg = celery_test_task.delay()
    return HttpResponse("<h3>Celery Test Works Well!</h3>")
