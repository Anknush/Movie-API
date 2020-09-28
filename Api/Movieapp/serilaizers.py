from rest_framework import serializers
from .models import Movie,Ratings
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=('id','username','password')
        extra_kwargs={'password':{'write_only':True,'required':True}}

    def create(self,validated_data):
        user=User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user
class MovieSerializers(serializers.ModelSerializer):
    class Meta:
        model=Movie
        fields=('id','title','description','no_of_rating','avg_rating')

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model=Ratings
        fields=('id','user','movie','stars')
