from rest_framework import serializers
from main.models import Lost_documents, Document_type


class DocumentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document_type
        fields = ("name", "has_an_expiration_date", "has_a_series")


class LostDocumentsSerializer(serializers.ModelSerializer):
    document_type = DocumentTypeSerializer()

    class Meta:
        model = Lost_documents
        fields = ("identifier", "document_series", "document_number", "document_type",
                  "status", "event_date", "date_of_recording", "registration_authority")
