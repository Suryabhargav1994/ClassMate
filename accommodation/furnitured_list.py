from rest_framework.views import APIView
from .models import furnitured
import uuid
from django.http import JsonResponse

class furnituredlist(APIView):
    def get(self, request):
        try:
            amenities = furnitured.objects.all()
            list_of_amenities = []
            for i in amenities:
                list_of_amenities.append({"amenity_id": i.amenity_id,
                                             "amenity_name": i.name})
            return JsonResponse(
                    {
                        "status": "200",
                        "message": "Aminity data has retrivied", 
                        "data": list_of_amenities
                    })
        except:
            return JsonResponse({
                    "status": "500",
                    "message": "Error with Aminity", 
                    "data": None
            })