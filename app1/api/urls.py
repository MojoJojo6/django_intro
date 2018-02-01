from django.urls import path
from .views import *

urlpatterns = [
    path('user/',user_List.as_view()),
    path('user/<int:id>', user_Detail.as_view())
]