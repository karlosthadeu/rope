from django.urls import path
from .views import ChamadosView

urlpatterns = [
    path('', ChamadosView.as_view(), name='teste')
]