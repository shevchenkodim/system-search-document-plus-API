from django.urls import path
from .views import Find_document

urlpatterns = [
    path('search/', Find_document.as_view()),
]