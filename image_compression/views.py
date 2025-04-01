from django.shortcuts import render, redirect
from django.http import HttpResponse

from .forms import CompressImageForm

# Pillow Lib
from PIL import Image
import io



def compress(request):
    user =  request.user

    if request.method == "POST":
        form = CompressImageForm(request.POST, request.FILES)
        if form.is_valid():

            original_img = form.cleaned_data["original_img"]
            quality = form.cleaned_data["quality"]

            compressed_image = form.save(commit=False)
            compressed_image.user = user

            # Perform compression with Pillow lib
            img = Image.open(original_img)
            output_format = img.format

            buffer = io.BytesIO()
            img.save(buffer, format=output_format, quality=quality)

            # Reset buffer position for furter write operations
            buffer.seek(0)

            # Save compressed image in model
            compressed_image.compressed_img.save(
                f"compressed_{original_img}", buffer
            )

            # Automaticaly download the compressed file
            response = HttpResponse(buffer.getvalue(), content_type=f"image/{output_format.lower()}")
            response["Content-Disposition"] = f"attachment; filename=compressed_{original_img}"
            return response

    else:

        form = CompressImageForm()

        context = {
            "form": form
        }

        return render(request, "image_compression/compress.html", context)