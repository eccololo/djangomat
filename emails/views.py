from django.shortcuts import render
from .forms import EmailForm


def send_email(request):

    if request.method == "POST":
        pass
    else:
        email_form = EmailForm()
        context = {
            "email_form": email_form
        }

        return render(request, "emails/sendemail.html", context)
