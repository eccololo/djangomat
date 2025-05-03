from django.shortcuts import render


def cheap_ebook(request):

    context = {

    }

    return render(request, "cheap_ebook/cheap-ebook.html", context)