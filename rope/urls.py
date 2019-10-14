from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from rope import settings

urlpatterns = [
    path('', include('nucleo.urls')),
    path('admin/', admin.site.urls),
    path('conta/', include('conta.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
