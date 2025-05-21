from django.shortcuts import render
from django.contrib import messages

from .utils import scrape_cheap_ebook
from .models import CheapBook

from pprint import pprint

def cheap_ebook_check(request):

    return render(request, "cheap_ebook/cheap-ebook-check.html")


def cheap_ebook(request):

    scraped_data = scrape_cheap_ebook()

    print("*" * 40)
    pprint(scraped_data)

    book, created = CheapBook.objects.get_or_create(
        title=scraped_data["title"],
        author_name=scraped_data["author_name"],
        defaults={
            "price": scraped_data["price"],
            "pages": scraped_data["pages"],
            "is_epub": scraped_data["is_epub"],
            "image_url": scraped_data["image_url"],
            "description": scraped_data["description"]
        }
    )

    if created:
         messages.success(request, f"This ebook was saved in web app DB.")
    else:
         messages.error(request, f"Could not save this ebook in web app DB.")

    context = {
        "ebook_data": scraped_data
    }

    return render(request, "cheap_ebook/cheap-ebook.html", context)