from django.contrib import admin
from django.urls import path
from nossaagua.views import FaltaAgua, LoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('faltaagua/', FaltaAgua),
    path('login/', LoginView.as_view()),
]
