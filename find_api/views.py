from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import LostDocumentsSerializer
from main.models import Lost_documents
import json


class Find_document(APIView):

    def get(self, request):
        data = request.GET.get('data')
        try:
            data_json = json.loads(data)

            series = data_json.get('search_phrase')[:2]
            number = data_json.get('search_phrase')[2:]

            if data_json.get('report_type') == 'full':
                document = Lost_documents.objects.get(
                    document_series=series, document_number=number)
                serializer = LostDocumentsSerializer(document)

                return Response(serializer.data)

            elif data_json.get('report_type') == 'compact':
                document = Lost_documents.objects.filter(
                    document_series=series, document_number=number)

                if document:
                    return Response({'result': '1'})
                else:
                    return Response({'result': '0'})
            else:
                return Response({'result': 'Error'})
        except Exception as e:
            return Response({'result': 'Error'})

# {"report_type": "full", "search_phrase": "AB149725"}
# {"report_type": "comppact", "search_phrase": "AB149725"}
