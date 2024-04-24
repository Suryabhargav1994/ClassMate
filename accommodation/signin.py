
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Person
from django.contrib.auth.hashers import check_password
from django.http import JsonResponse


class SignIn(APIView):
    def post(self, request):
        data = request.data
        email = data.get('email')
        password = data.get('password')

        user = Person.objects.filter(email=email).first()
        print(check_password(password, user.password))
        if user is not None and check_password(password, user.password):

            return JsonResponse(
            {
                "status": "200",
                "message": "Login succefful", 
                "data": {"user_id":user.person_id}
            })
        else:
            return JsonResponse(
            {
                "status": "401",
                "message": "Invalid crendentials", 
                "data": None
            })