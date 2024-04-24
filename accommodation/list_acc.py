from rest_framework.views import APIView
from .models import Accomidation, Universities, UniversitiesDistances
import uuid
from django.http import JsonResponse

class ListAccomidation(APIView):
    def post(self, request):
        try:
            data = request.data
            university_id = data.get('university_id')
            uni_id = Universities.objects.filter(university_id = university_id)
            
            university_list = [i for i in uni_id]
            acc_ids_list = UniversitiesDistances.objects.filter(university_id__in = university_list)
            acc_ids = [i.accomidation_id.accomidation_id for i in acc_ids_list]
            acc_data = Accomidation.objects.filter(accomidation_id__in = acc_ids)
            data_list = []
            for acc in acc_data:
                total_distace = UniversitiesDistances.objects.filter(accomidation_id = acc.accomidation_id).first()
                data_list.append({"accomidation_name": acc.name,
                                  "price": acc.price,
                                  "availability": acc.availability,
                                  "username": acc.person_id.firstname,
                                  "distance": str(total_distace.distance)+" kms",
                                  "accomidation_id": acc.accomidation_id,
                                  "furnished": acc.furnituredname
                                  })
            
            return JsonResponse(
                    {
                        "status": "200",
                        "message": "List of accomidation data", 
                        "data": data_list
                    })
        except Exception as e:
            return JsonResponse({
                    "status": "401",
                    "message": "Error with getting Accomidation", 
                    "data": str(e)
            })