from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings
from .forms import EmailForm
from dataentry.utils import send_email_notification
from .models import Subscriber, Email
from .tasks import send_email_task


def send_email(request):
    """This is a view for sending bulk emails."""
    if request.method == "POST":
        email_form = EmailForm(request.POST, request.FILES)
        if email_form.is_valid():
            email_form = email_form.save()

            subject = request.POST.get("subject")
            message = request.POST.get("body")
            email_list = request.POST.get("email_list")
            email_list = email_form.email_list

            subscribers = Subscriber.objects.filter(email_list=email_list)
            to_email = [email.email_address for email in subscribers]

            if email_form.attachment:
                attachment = email_form.attachment.path
            else:
                attachment = None
            
            # Celery task.
            send_email_task.delay(subject, message, to_email, attachment)

            messages.success(request, "Email sent succesfully!")
            return redirect("send_email")
    else:
        email_form = EmailForm()
        context = {
            "email_form": email_form
        }

        return render(request, "emails/sendemail.html", context)


def track_click(request):
    """This is a view for tracking clicks on the links send in email."""
    pass


def track_open(request):
    """This is a view for tracking number of opened emails which were send in bulk mode."""


def track_dashboard(request):
    """View for dashboard of tracing email feature."""

    emails = Email.objects.all()
    context = {
        "emails": emails
    }

    return render(request, "emails/track_dashboard.html", context)