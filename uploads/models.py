from django.db import models

class Upload(models.Model):

    model_name = models.CharField(max_length=70)
    file = models.FileField(upload_to=f"uploads/")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.model_name

