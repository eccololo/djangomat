from django.shortcuts import render, redirect
from uploads.models import Upload
from django.conf import settings
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
from .tasks import import_data_task
from .utils import get_all_custom_models


# @method_decorator(csrf_protect, name='dispatch')
# @method_decorator(login_required, name='dispatch')
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

        # Celery task here ...
        import_data_task.delay(corrected_path, model_name)
        messages.success(request, "Your data is being imported. You will be notified once it is done!")

        return redirect("import_data")
    else:
        custom_models = get_all_custom_models()
        context = {
            "custom_models": custom_models
        }

        return render(request, "dataentry/importdata.html", context)
