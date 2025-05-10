from django.contrib import admin
from .models import Image

# Register your models here.


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ("id", "image", "uploaded_at")
    search_fields = ("id",)
    list_filter = ("uploaded_at",)
    ordering = ("-uploaded_at",)
