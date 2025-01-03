from django.shortcuts import render


def send_email(request):
    return render(request, "emails/sendemail.html")
