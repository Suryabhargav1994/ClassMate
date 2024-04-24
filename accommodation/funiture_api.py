from rest_framework.views import APIView
from .models import furnitured
import uuid
from django.http import JsonResponse

class FurnitureApi(APIView):
    def post(self, request):
        try:
            data = request.data
            funrniture_name = data.get('name')
            funrniture_name = funrniture_name.lower()
            print(funrniture_name)
            exis_amenity = furnitured.objects.filter(name = funrniture_name).count()
            if exis_amenity == 0:
                funrniture_data = furnitured(furnitured_id= uuid.uuid4(), name = funrniture_name)
                funrniture_data.save()

                return JsonResponse(
                    {
                        "status": "200",
                        "message": "funrniture data has registered", 
                        "data": None
                    })
            else:
                return JsonResponse(
                    {
                        "status": "401",
                        "message": "funrniture already exists", 
                        "data": None
                    })
        except:
            return JsonResponse({
                    "status": "401",
                    "message": "Error with funrniture", 
                    "data": None
            })