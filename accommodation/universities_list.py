from rest_framework.views import APIView
from .models import Universities
import uuid
from django.http import JsonResponse

class Universitylist(APIView):
    def get(self, request):
        try:
            universities = Universities.objects.all()
            list_of_universities = []
            for i in universities:
                list_of_universities.append({"university_id": i.university_id,
                                             "university_name": i.university_name,
                                             "university_address": i.address})
            return JsonResponse(
                    {
                        "status": "200",
                        "message": "University data has registered", 
                        "data": list_of_universities
                    })
        except:
            return JsonResponse({
                    "status": "500",
                    "message": "Error with university", 
                    "data": None
            })