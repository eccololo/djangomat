from django.contrib import admin
from django.utils.html import format_html

from .models import CompressImage



class CompressImageAdmin(admin.ModelAdmin):

    def thumbnail(self, obj):

        return format_html(f"<img src='{ obj.compressed_img.url }' width='40' height='40'>")

    def org_image_size(self, obj):

        return format_html("{}MB", f"{obj.original_img.size / (1024 * 1024):.2f}")
    
    def comp_image_size(self, obj):

        size_in_mb = obj.compressed_img.size / (1024 * 1024)
        if size_in_mb > 1:
            return format_html("{}MB", f"{size_in_mb:.2f}")
        else:
            size_in_kb = obj.compressed_img.size / 1024
            return format_html("{}KB", f"{size_in_kb:.2f}")



    list_display = ["user", "thumbnail", "org_image_size", "comp_image_size", "compressed_at"]

admin.site.register(CompressImage, CompressImageAdmin)

