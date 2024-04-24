from rest_framework.views import APIView
from .models import Accomidation, Person
import uuid
from django.http import JsonResponse

class AccommidationApi(APIView):
    def post(self, request):
        try:
            data = request.data
            acc_name = data.get('name')
            acc_address = data.get('address')
            acc_price = data.get('price')
            availability = data.get('availability')
            person_id = data.get('person_id')
            persons_id = Person.objects.filter(person_id = person_id).first()
            exis_acc = Accomidation.objects.filter(name = acc_name).count()
            if exis_acc == 0:
                acc_id = uuid.uuid4()
                acc_data = Accomidation(accomidation_id= acc_id, 
                                            name = acc_name,
                                            address = acc_address,
                                            price = acc_price,
                                            availability = availability,
                                            person_id = persons_id,
                                            furnituredname = data.get('furnituredname')
                                            )
                acc_data.save()

                return JsonResponse(
                    {
                        "status": "200",
                        "message": "Accomidation data has registered", 
                        "data": {"acc_id" : str(acc_id)}
                    })
            else:
                return JsonResponse(
                    {
                        "status": "401",
                        "message": "Accomidation already exists", 
                        "data": None
                    })
        except Exception as e:
            return JsonResponse({
                    "status": "401",
                    "message": "Error with Accomidation", 
                    "data": str(e)
            })