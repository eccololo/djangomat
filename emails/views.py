from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import EmailForm
from .models import Subscriber, Email
from .tasks import send_email_task
from django.db.models import Sum


def send_email(request):
    """This is a view for sending bulk emails."""
    if request.method == "POST":
        email_form = EmailForm(request.POST, request.FILES)
        if email_form.is_valid():
            email = email_form.save()

            subject = request.POST.get("subject")
            message = request.POST.get("body")
            email_list = request.POST.get("email_list")
            email_list = email.email_list

            subscribers = Subscriber.objects.filter(email_list=email_list)
            to_email = [email.email_address for email in subscribers]

            if email.attachment:
                attachment = email.attachment.path
            else:
                attachment = None
            
            email_id = email.id

            # Celery task.
            send_email_task.delay(subject, message, to_email, attachment, email_id)

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
    """View for dashboard of tracking email feature."""

    emails = Email.objects.all().annotate(total_sent=Sum('sent__total_sent'))
    context = {
        "emails": emails
    }

    return render(request, "emails/track_dashboard.html", context)


def track_stats(request, pk):
    """View for tracking email stats."""
    email = get_object_or_404(Email, pk=pk)
    context = {
        "email": email
    }
    return render(request, "emails/track_stats.html", context)