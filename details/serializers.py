from rest_framework import serializers

from django.contrib.auth import get_user_model
from .models import Exercises,Schedule,User
from rest_framework.response import Response

#serialziers convert python object into proper json object for transport accross network
class UserCreateSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email = validated_data['email'],
            goal = validated_data['goal'],
            )
        user.set_password(validated_data['password'])
        user.save()
        return user

    class Meta:
        model = User
        fields = ['id','email','username','password','goal']
        extra_kwargs = {'password': {'write_only': True}}


class ExerciseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Exercises
        fields = '__all__'



class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = ['User','time_rest','exc_time','exerciselist']
        extra_kwargs = {'User': {'read_only': True}}
