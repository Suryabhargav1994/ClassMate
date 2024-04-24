from django.urls import path

from . import signup, signin, university_register, universities_list, amenity_register, amenities_list, edit_accomidation
from . import accommidation_reg, uni_acc_map, list_acc, booking_room, acco_details, funiture_api, furnitured_list, delete_accomidation

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
        path('booking-room', booking_room.BookAccomidation.as_view()),
        path('account-details', acco_details.PersonDetails.as_view()),
        path('furniture-register', funiture_api.FurnitureApi.as_view()),
        path('furniture-list', furnitured_list.furnituredlist.as_view()),
        path('edit-accomidation', edit_accomidation.EditAccomidation.as_view()),
        path('delete-accomidation', delete_accomidation.DeleteAccomidation.as_view())
        
    ]