from django.shortcuts import render

from .utils import scrape_cheap_ebook

from pprint import pprint

def cheap_ebook_check(request):


    return render(request, "cheap_ebook/cheap-ebook-check.html")


def cheap_ebook(request):

    scraped_data = scrape_cheap_ebook()

    print("*" * 40)
    pprint(scraped_data)

    context = {

    }

    return render(request, "cheap_ebook/cheap-ebook.html", context)