from rest_framework import serializers
from .models import *
from django.contrib.auth.hashers import make_password

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = "__all__"


class UserSerialzer(serializers.ModelSerializer):
    cars = CarSerializer(many=True, read_only=True)
    class Meta:
        model = User
        fields = ["id", "username", "first_name", "last_name", "country", "cars", "street", "ph_no"]
    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super(UserSerialzer, self).create(validated_data)


    def validate(self, data):
        cars = data.get("cars")
    
        if not cars:


            raise serializers.ValidationError("please enter a atleast 1 vehicle")

        for car in cars:
            print(car)
            obj = Car.objects.get(id=car.id)
            if obj.owner.all():
                print("True")
                raise serializers.ValidationError("Enter your own vechicle")



        return data


class AdsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ads
        fields= "__all__"

