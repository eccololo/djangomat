from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from dataentry.tasks import celery_test_task
from .forms import RegistrationForm

def home(request):
    return render(request, "home.html", {})


def celery_test(request):
    msg = celery_test_task.delay()
    return HttpResponse("<h3>Celery Test Works Well!</h3>")

def register(request):

    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration succesfull!")
            return redirect("register")
        else:
            context = {
                 'form': form
            }
            return render(request, 'register.html', context)
    else:
        form = RegistrationForm()
        context = {
            'form': form
        }

    return render(request, "register.html", context)

def login(request):
    return render(request, "login.html")
