from rest_framework.views import APIView
from .models import Universities
import uuid
from django.http import JsonResponse

class UniversityApi(APIView):
    def post(self, request):
        try:
            data = request.data
            univ_name = data.get('university_name')
            address = data.get('address')
            exis_univ = Universities.objects.filter(university_name = univ_name).count()
            if exis_univ == 0:
                university_data = Universities(university_id= uuid.uuid4(), university_name = univ_name, address = address)
                university_data.save()

                return JsonResponse(
                    {
                        "status": "200",
                        "message": "University data has registered", 
                        "data": None
                    })
            else:
                return JsonResponse(
                    {
                        "status": "401",
                        "message": "University already exists", 
                        "data": None
                    })
        except:
            return JsonResponse({
                    "status": "401",
                    "message": "Error with university", 
                    "data": None
            })