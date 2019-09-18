from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('conta/', include('conta.urls')),
    path('', include('nucleo.urls')),
]
