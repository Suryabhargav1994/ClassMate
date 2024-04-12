from django.urls import path

from . import signup, signin, university_register, universities_list, amenity_register, amenities_list

urlpatterns = [
        path('signup', signup.SignUp.as_view()),
        path('signin', signin.SignIn.as_view()),
        path('university-registry', university_register.UniversityApi.as_view()),
        path('universities-list', universities_list.Universitylist.as_view()),
        path('aminity-registry', amenity_register.AmenityApi.as_view()),
        path('aminity-list', amenities_list.Aminitylist.as_view())
    ]