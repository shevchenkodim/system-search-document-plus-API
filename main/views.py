from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView
from django.urls import reverse
from .tasks import load_data_structure_task
from datetime import datetime
from .models import Lost_documents


class IndexView(TemplateView):
    template_name = "base.html"
    extra_context = {}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # load_data_structure_task.apply_async()
        return context


class SearchView(TemplateView):
    template_name = "document_search_result.html"
    extra_context = {}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        document_series = self.request.GET.get('series')
        document_number = self.request.GET.get('number')
        document_series_and_number = self.request.GET.get('series_and_number')

        if document_series and document_number:
            document = Lost_documents.objects.filter(
                document_series=document_series, document_number=document_number)
            context['documents'] = document

        elif document_series_and_number:
            document_series_and_number
            series = document_series_and_number[:2]
            number = document_series_and_number[2:]
            document = Lost_documents.objects.filter(
                document_series=series, document_number=number)
            context['documents'] = document

        return context
