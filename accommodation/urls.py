from django.urls import path

from . import signup, signin, university_register, universities_list, amenity_register, amenities_list
from . import accommidation_reg, uni_acc_map, list_acc, booking_room

urlpatterns = [
        path('signup', signup.SignUp.as_view()),
        path('signin', signin.SignIn.as_view()),
        path('university-registry', university_register.UniversityApi.as_view()),
        path('universities-list', universities_list.Universitylist.as_view()),
        path('aminity-registry', amenity_register.AmenityApi.as_view()),
        path('aminity-list', amenities_list.Aminitylist.as_view()),
        path('accommodation-register', accommidation_reg.AccommidationApi.as_view()),
        path('acc-uni-map', uni_acc_map.AccUnivApi.as_view()),
        path('acc-list', list_acc.ListAccomidation.as_view()),
        path('booking-room', booking_room.BookAccomidation.as_view())
    ]