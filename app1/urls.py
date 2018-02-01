from django.urls import path
from .views import Index

urlpatterns = [
    path('app1/',Index.as_view())
]
