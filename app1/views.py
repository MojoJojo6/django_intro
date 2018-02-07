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


class Eligible(TemplateView):
    template_name='eligible.html'



class NotEligible(TemplateView):
    template_name='notEligible.html'
