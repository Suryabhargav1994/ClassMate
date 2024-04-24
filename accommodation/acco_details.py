from rest_framework.views import APIView
from .models import Person
import uuid
from django.http import JsonResponse

class PersonDetails(APIView):
    def post(self, request):
        # try:
            data = request.data
            person_id = data.get('person_id')
            print(person_id, "this is id")
            persons_id = Person.objects.filter(person_id = person_id).values_list('firstname', "lastname", "phone_number")
            person_list = []
            print(persons_id)
            for per in persons_id:
                  person_list.append({
                        "firstname": per[0],
                        "lastname": per[1],
                        "phone_number": per[2]
                  })
            return JsonResponse(
                    {
                        "status": "200",
                        "message": "user details", 
                        "data": person_list
                    })
        # except Exception as e:
        #     return JsonResponse({
        #             "status": "401",
        #             "message": "Error with user details", 
        #             "data": str(e)
        #     })
            