from rest_framework.views import APIView
from .models import Amenities
import uuid
from django.http import JsonResponse

class AmenityApi(APIView):
    def post(self, request):
        try:
            data = request.data
            amenity_name = data.get('amenity_name')
            amenity_name = amenity_name.lower()
            print(amenity_name)
            exis_amenity = Amenities.objects.filter(name = amenity_name).count()
            if exis_amenity == 0:
                amenity_data = Amenities(amenity_id= uuid.uuid4(), name = amenity_name)
                amenity_data.save()

                return JsonResponse(
                    {
                        "status": "200",
                        "message": "Amenity data has registered", 
                        "data": None
                    })
            else:
                return JsonResponse(
                    {
                        "status": "401",
                        "message": "Amenity already exists", 
                        "data": None
                    })
        except:
            return JsonResponse({
                    "status": "401",
                    "message": "Error with Amenity", 
                    "data": None
            })