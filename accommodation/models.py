from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
import uuid
from rest_framework.authtoken.models import Token
from django.conf import settings



class Person(AbstractBaseUser):

    person_id = models.UUIDField(default = uuid.uuid4(), primary_key = True)
    email = models.EmailField(verbose_name='email', unique=True, null = False)
    password = models.CharField(max_length=225, null = False, default= 'password')
    firstname = models.CharField(max_length=250)
    lastname = models.CharField(max_length=250)
    is_active = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=250, default="")
    date_added = models.DateField(auto_now_add = True)
    last_modified = models.DateField(auto_now = True)

class Universities(models.Model):
    
    university_id = models.UUIDField(default = uuid.uuid4(), primary_key = True)
    university_name = models.CharField(max_length=255, null = False)
    address = models.CharField(max_length = 250)
    date_added = models.DateField(auto_now_add = True)
    last_modified = models.DateField(auto_now = True)

class Amenities(models.Model):

    amenity_id = models.UUIDField(default = uuid.uuid4(), primary_key = True)
    name = models.CharField(max_length = 255)
    date_added = models.DateField(auto_now_add = True)
    last_modified = models.DateField(auto_now = True)

class furnitured(models.Model):
    furnitured_id = models.UUIDField(default = uuid.uuid4(), primary_key = True)
    name = models.CharField(max_length=255)
    date_added = models.DateField(auto_now_add = True)
    last_modified = models.DateField(auto_now = True)
class Accomidation(models.Model):

    accomidation_id = models.UUIDField(default = uuid.uuid4(), primary_key = True)
    name = models.CharField(max_length = 255, null = False)
    address = models.CharField(max_length = 255)
    price = models.IntegerField()
    availability = models.IntegerField()
    date_added = models.DateField(auto_now_add = True)
    last_modified = models.DateField(auto_now = True)
    person_id = models.ForeignKey(Person, db_column = 'person_id', on_delete=models.CASCADE)
    furnituredname = models.CharField(max_length = 255)
    

class UniversitiesDistances(models.Model):
    id = models.UUIDField(default=uuid.uuid4(), primary_key=True)
    university_id = models.ForeignKey(Universities, db_column = "university_id", on_delete = models.CASCADE)
    accomidation_id = models.ForeignKey(Accomidation, db_column = 'accomidation_id', on_delete=models.CASCADE)
    distance = models.CharField(max_length = 255)

class AccomidationAmenities(models.Model):

    id = models.UUIDField(default = uuid.uuid4(), primary_key = True)
    accomidation_id = models.ForeignKey(Accomidation, db_column = "accomidation_id", on_delete = models.CASCADE)
    amenity_id = models.ForeignKey(Amenities, db_column = "amenity_id", on_delete = models.CASCADE)
    date_added = models.DateField(auto_now_add = True)
    last_modified = models.DateField(auto_now = True)

class BookingDetails(models.Model):

    booking_id = models.UUIDField(default = uuid.uuid4(), primary_key = True)
    person_id = models.ForeignKey(Person, db_column = 'person_id', on_delete = models.CASCADE)
    date_added = models.DateField(auto_now_add = True)
    last_modified = models.DateField(auto_now = True)