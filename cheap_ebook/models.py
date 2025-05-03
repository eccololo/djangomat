from django.db import models


class CheapBook(models.Model):

    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    author_name = models.CharField(max_length=255)
    pages = models.PositiveIntegerField()
    is_epub = models.BooleanField(default=True)
    image_url = models.URLField(max_length=500, blank=True)
    author_desc = models.TextField(max_length=1000)
    description = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:

        verbose_name = "Cheap Book"
        verbose_name_plural = "Cheap Books"


    def __str__(self):
        return f"{self.title} by {self.author_name} for {self.price}zł"
