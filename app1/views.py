from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.http import JsonResponse

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import ensure_csrf_cookie

from .models import *

# Create your views here.

method_decorator(ensure_csrf_cookie,'dispatch')
class Index(TemplateView):
    template_name='index.html'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def post(self, request, *args, **kwargs):
        print(request.POST)
        return JsonResponse({})
