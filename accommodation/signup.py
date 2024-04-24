
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.generics import GenericAPIView
from django.contrib.auth.hashers import make_password
from .models import Person
import uuid
from django.http import JsonResponse
class SignUp(ObtainAuthToken, GenericAPIView):

    def post(self, request):
        data = request.data
        firstname = data.get('firstname')
        lastname = data.get('lastname')
        email = data.get('email')
        password = data.get('password')
        phone_number = data.get('phone_number')

        userid = uuid.uuid4()
        person_data = Person.objects.filter(email = email).count()
        print(person_data)
        if person_data == 0:
            account_save = Person( person_id=userid, firstname=firstname, lastname=lastname, email=str(email).lower(),
                                        password=make_password(password), phone_number = phone_number)
            account_save.save()

            return JsonResponse(
            {
                "status": "200",
                "message": "Data saved successfully", 
                "data": None
            })
        else:
            return JsonResponse(
            {
                "status": "401",
                "message": "Email already exist", 
                "data": None
            }
            )
    