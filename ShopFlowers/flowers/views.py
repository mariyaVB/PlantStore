from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from .models import Flowers, Category
from datetime import datetime
from django.views import View
from django.views.generic import TemplateView, ListView


class MainPage(View):
    def get(self, request):
        return render(request, 'main_page.html')

    def post(self, request):
        pass


class FlowersView(ListView):
    model = Flowers
    template_name = 'flowers.html'
    context_object_name = 'flowers'

    def get_queryset(self):
        return Flowers.objects.all()






