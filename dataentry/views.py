from django.shortcuts import render

def import_data(request):
    
    if request.method == "POST":
        pass
    else:
        all_models = pass

    return render(request, "dataentry/importdata.html", {})
