from django.shortcuts import render, redirect
from uploads.models import Upload
from django.conf import settings
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
from django.core.management import call_command
from .tasks import import_data_task
from .utils import get_all_custom_models
from dataentry.utils import check_csv_errors


@csrf_protect
@login_required
def import_data(request):

    if request.method == "POST":
        file_path = request.FILES.get("file_path")
        model_name = request.POST.get("model_name")

        upload = Upload.objects.create(model_name=model_name, file=file_path)

        relative_path = str(upload.file.url)
        base_url = str(settings.BASE_DIR)

        file_path = base_url + relative_path

        corrected_path = file_path.replace("/", "\\")

        # Check for CSV errors
        try:
            check_csv_errors(corrected_path, model_name)
        except Exception as e:
            messages.error(request, str(e))
            return redirect("import_data")

        # Celery task here
        import_data_task.delay(corrected_path, model_name)
        messages.success(request, "Your data is being imported. You will be notified once it is done!")

        return redirect("import_data")
    else:
        custom_models = get_all_custom_models()
        context = {
            "custom_models": custom_models
        }

        return render(request, "dataentry/importdata.html", context)



def export_data(request):

    if request.method == "POST":
        model_name = request.POST.get("model_name")

        filename = f"exported-{model_name.lower()}.csv"
        
        try:
            call_command("exportdata",filename, model_name)
        except Exception as e:
            raise e
        
        messages.success(request, "Your data has been exported and send to your email!")
        return redirect("export_data")
    else:
        custom_models = get_all_custom_models()
        context = {
            "custom_models": custom_models
        }
        return render(request, "dataentry/exportdata.html", context)