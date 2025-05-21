from django.db import models
from django.utils.safestring import mark_safe


class CheapBook(models.Model):

    title = models.CharField(max_length=255)
    price = models.CharField(max_length=10)
    author_name = models.CharField(max_length=255)
    pages = models.PositiveIntegerField()
    is_epub = models.BooleanField(default=True)
    image_url = models.URLField(max_length=500, blank=True)
    description = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:

        verbose_name = "Cheap Book"
        verbose_name_plural = "Cheap Books"


    def __str__(self):
        return f"{self.title} by {self.author_name} for {self.price}"
    
    def formatted_description(self):

        """For better looking desc in admin panel model field."""

        text = self.description.strip()

        if text.startswith('[') and text.endswith(']'):

            items = text[1:-1].split("', '")

            items[0] = items[0].lstrip("'").strip()
            items[-1] = items[-1].rstrip("'").strip()

            items = [item.strip() for item in items if item.strip()]
            items = items[:-2]

            html = ''.join(f'<p>{item.strip()}</p>' for item in items if item.strip())

            return mark_safe(html)

        return self.description

    formatted_description.short_description = "Desc"
