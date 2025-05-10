from django.shortcuts import render, redirect, get_object_or_404
from .forms import ImageUploadForm
from .models import Image
from django.views.decorators.csrf import csrf_protect

@csrf_protect
def home(request):
    if request.method == "POST":
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("home")  # Avoid re-posting on refresh
    else:
        form = ImageUploadForm()
    
    images = Image.objects.all().order_by('-uploaded_at')
    return render(request, "uploder/home.html", {"form": form, "images": images})


def delete_image(request, pk):
    image = get_object_or_404(Image, pk=pk)
    image.delete()
    return redirect("home")


def image_detail(request, image_id):
    image = get_object_or_404(Image, id=image_id)
    
    # Increment the views count
    image.increment_views()
    
    return render(request, "uploder/image_detail.html", {"image": image})
