from rest_framework.views import APIView
from .models import Accomidation, Universities, UniversitiesDistances
import uuid
from django.http import JsonResponse

class BookAccomidation(APIView):
    def post(self, request):
        try:
            data = request.data
            accomidation_id = data.get('accomidation_id')
            total_room = data.get('total_room')
            acc_data = Accomidation.objects.filter(accomidation_id = accomidation_id).first()

            
            if acc_data.availability > total_room:
                acc_data.availability = acc_data.availability - total_room
                acc_data.save()
            
                return JsonResponse(
                        {
                            "status": "200",
                            "message": "Accomidation has completly booked", 
                            "data": None
                        })
            else:
                return JsonResponse({
                    "status": "401",
                    "message": "Selected number of rooms are not available", 
                    "data": None
                })
        except Exception as e:
            return JsonResponse({
                    "status": "401",
                    "message": "Error with getting Accomidation", 
                    "data": str(e)
            })
            