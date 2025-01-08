from django.db import models
from ckeditor.fields import RichTextField

class List(models.Model):

    email_list = models.CharField(max_length=35)

    def __str__(self):
        return self.email_list
    

class Subscriber(models.Model):

    email_address = models.EmailField(max_length=50)
    # When list will be deleted as well deleted will be subscriber.
    email_list = models.ForeignKey(List, on_delete=models.CASCADE)

    def __str__(self):
        return self.email_address

class Email(models.Model):

    subject = models.CharField(max_length=100)
    body = RichTextField()
    attachment = models.FileField(upload_to="email_attachments/", blank=True)
    sent_at = models.DateTimeField(auto_now_add=True)

    email_list = models.ForeignKey(List, on_delete=models.CASCADE)

    def __str__(self):
        return self.subject