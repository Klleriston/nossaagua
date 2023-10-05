from django.contrib import admin
from django.urls import path
from nossaagua.views import FaltaAgua

urlpatterns = [
    path('admin/', admin.site.urls),
    path('faltaagua/', FaltaAgua),
]
