from django.contrib import admin
from .models import Upload

class UploadAdmin(admin.ModelAdmin):

    list_display = ["model_name", "uploaded_at"]
    list_filter = ["model_name"]

admin.site.register(Upload, UploadAdmin)