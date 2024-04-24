from rest_framework.views import APIView
from .models import Accomidation, Universities, UniversitiesDistances
import uuid
from django.http import JsonResponse

class DeleteAccomidation(APIView):
    def post(self, request):
        try:
            data = request.data
            accomidation_id = data.get('accomidation_id')
            acc_data = Accomidation.objects.filter(accomidation_id = accomidation_id).first()
            acc_data.delete()
            return JsonResponse(
                    {
                        "status": "200",
                        "message": "Accomidation has Deleted", 
                        "data": None
                    })
        except Exception as e:
            return JsonResponse({
                    "status": "401",
                    "message": "Error with  Accomidation delete", 
                    "data": str(e)
            })
            