from rest_framework.views import APIView
from .models import Accomidation, Universities, UniversitiesDistances
import uuid
from django.http import JsonResponse

class AccUnivApi(APIView):
    def post(self, request):
        try:
            data = request.data
            university_id = data.get('university_id')
            accomidation_id = data.get('accomidation_id')
            distance = data.get('distance')
            uni_id = Universities.objects.filter(university_id = university_id).first()
            acc_id = Accomidation.objects.filter(accomidation_id = accomidation_id).first()
            exis_data = UniversitiesDistances.objects.filter(university_id= uni_id, accomidation_id=acc_id).count()
            if exis_data == 0:
                acc_data = UniversitiesDistances(id= uuid.uuid4(), 
                                            university_id = uni_id,
                                            accomidation_id = acc_id,
                                            distance = distance  
                                            )
                acc_data.save()

                return JsonResponse(
                        {
                            "status": "200",
                            "message": "Accomidation data has registered", 
                            "data": None
                        })
            else:
                return JsonResponse(
                {
                    "status": "401",
                    "message": "Acc already exist", 
                    "data": None
                })
        except Exception as e:
            return JsonResponse({
                    "status": "401",
                    "message": "Error with Accomidation", 
                    "data": str(e)
            })