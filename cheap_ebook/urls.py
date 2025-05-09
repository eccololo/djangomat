from django.urls import path
from . import views


urlpatterns = [
    path('ebook-check/', views.cheap_ebook_check, name="cheap-ebook-check"),
    path('ebook-details/', views.cheap_ebook, name="cheap-ebook")
]