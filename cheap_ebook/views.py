from django.shortcuts import render

from .utils import scrape_cheap_ebook

def cheap_ebook(request):

    scraped_data = scrape_cheap_ebook()

    context = {

    }

    return render(request, "cheap_ebook/cheap-ebook.html", context)