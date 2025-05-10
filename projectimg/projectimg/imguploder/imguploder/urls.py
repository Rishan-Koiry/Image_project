from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from uploder import views

urlpatterns = [
    path('', views.home, name='home'),
path('image/<int:image_id>/', views.image_detail, name='image_detail'),
path('delete/<int:pk>/', views.delete_image, name='delete_image'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
