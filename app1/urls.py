from django.urls import path
from .views import Index, Eligible, NotEligible

urlpatterns = [
    path('app1/',Index.as_view()),
    path('app1/eligible/', Eligible.as_view()),
    path('app1/noteligible/', NotEligible.as_view())
]
