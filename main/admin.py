from django.contrib import admin
from .models import Document_type, Lost_documents


@admin.register(Document_type)
class Document_typeAdmin(admin.ModelAdmin):
    list_display = ('name', 'has_an_expiration_date', 'has_a_series')


@admin.register(Lost_documents)
class Lost_documentsAdmin(admin.ModelAdmin):
    list_display = ('identifier', 'document_series', 'document_number', 'document_type',
                    'status', 'event_date', 'date_of_recording', 'registration_authority')
