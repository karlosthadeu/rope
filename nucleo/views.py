from django.shortcuts import render, HttpResponse
from django.views import View
from django.http import JsonResponse

# Create your views here.
class ChamadosView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Hello World')

class HistoricosView():
    pass

class MateriaisView():
    pass

class PlanosDeEstudosView():
    pass

class PublicacoesView():
    pass