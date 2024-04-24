from rest_framework.views import APIView
from .models import Accomidation, Universities, UniversitiesDistances
import uuid
from django.http import JsonResponse

class EditAccomidation(APIView):
    def post(self, request):
        try:
            data = request.data
            accomidation_id = data.get('accomidation_id')
            accomidation_name = data.get('name')
            acc_data = Accomidation.objects.filter(accomidation_id = accomidation_id).first()

            acc_data.name = accomidation_name
            acc_data.save()
            return JsonResponse(
                    {
                        "status": "200",
                        "message": "Accomidation details has updated", 
                        "data": None
                    })
        except Exception as e:
            return JsonResponse({
                    "status": "401",
                    "message": "Error with  Accomidation update", 
                    "data": str(e)
            })
            