from django.contrib import admin
from django import forms
from django.utils.html import format_html

from .models import CheapBook



class CheapBookForm(forms.ModelForm):
    class Meta:
        model = CheapBook
        fields = "__all__"
        widgets = {
            "author_desc": forms.Textarea(attrs={"rows": 3}),
            "description": forms.Textarea(attrs={"rows": 4}),
        }



class CheapBookAdmin(admin.ModelAdmin):

    form = CheapBookForm

    def thumbnail(self, obj):

        if obj.image_url:

            return format_html(f"<img src='{obj.image_url}' width='40' height='40'>")
        
        return "No image"
    
    thumbnail.short_description = "Cover"

    list_display = ["title", "thumbnail", "author_name", "pages", "is_epub", "created_at"]
    search_fields = ["title", "author_name"]
    readonly_fields = [
    "title", "price", "author_name", "pages", "is_epub",
    "image_url", "author_desc", "description", "created_at"]

admin.site.register(CheapBook, CheapBookAdmin)
