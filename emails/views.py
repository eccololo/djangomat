from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import EmailForm
from .models import Subscriber, Email, Sent, EmailTracking
from .tasks import send_email_task
from django.db.models import Sum
from django.utils import timezone


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


def track_click(request, email_id):
    """This is a view for tracking clicks on the links send in email."""
    try:
        email_tracking = EmailTracking.objects.get(email_id=email_id)
        url = request.GET.get("url")
        # Check is clicked_at is already set or not.
        if not email_tracking.clicked_at:
            email_tracking.clicked_at = timezone.now()
            email_tracking.save()
            return HttpResponseRedirect(url)
        else:
            return HttpResponseRedirect(url) 
    except:
        return HttpResponse("Email tracking ID not found!") 


def track_open(request, email_id):
    """This is a view for tracking number of opened emails which were send in bulk mode."""
    try:
        email_tracking = EmailTracking.objects.get(email_id=email_id)
        # Check is opened_at is already set or not.
        if not email_tracking.opened_at:
            # Save current timestamp
            email_tracking.opened_at = timezone.now()
            email_tracking.save()
            return HttpResponse("Email opened succesfully!")
        else:
            print("Email already opened!")
            return HttpResponse("Email already opened!")
    except:
        return HttpResponse("Email tracking ID not found!")

def track_dashboard(request):
    """View for dashboard of tracking email feature."""

    emails = Email.objects.all().annotate(total_sent=Sum('sent__total_sent')).order_by("-sent_at")
    context = {
        "emails": emails
    }

    return render(request, "emails/track_dashboard.html", context)


def track_stats(request, pk):
    """View for tracking email stats."""
    email = get_object_or_404(Email, pk=pk)
    sent = Sent.objects.get(email=email)

    context = {
        "email": email,
        "total_sent": sent.total_sent
    }
    return render(request, "emails/track_stats.html", context)