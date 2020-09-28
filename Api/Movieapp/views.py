from django.shortcuts import render
from rest_framework import viewsets,status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,AllowAny
from .models import *
from .serilaizers import MovieSerializers,RatingSerializer,UserSerializers
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
# Create your views here

class UserViewset(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class=UserSerializers
    permission_classes = (AllowAny,)

class MovieViewset(viewsets.ModelViewSet):
    queryset=Movie.objects.all()
    serializer_class=MovieSerializers
    authentication_classes=(TokenAuthentication ,)
    permission_classes=(IsAuthenticated,)
    @action(detail=True,methods=["POST"])
    def rate_movie(self,request,pk=None):
        if 'stars' in request.data:
            movie=Movie.objects.get(id=pk)
            stars=request.data['stars']
            user=request.user
            print("User",user)

            # user=User.objects.get(id=1)
            print("user:",user.username)
            print("Movie Title is:",movie.title)
            try:
                rating=Ratings.objects.get(user=user.id,movie=movie.id)
                rating.stars=stars
                rating.save()
                serializer=RatingSerializer(rating,many=False)
                render={"Message":"Rating Updated","result":serializer.data}
                return Response(render,status=status.HTTP_200_OK)
            except:
                rating=Ratings.objects.create(user=user,movie=movie,stars=stars)
                serializer=RatingSerializer(rating,many=False)
                render={"Message":"Rating Created","result":serializer.data}
                return Response(render,status=status.HTTP_200_OK)



        else:
            render={"Message":"Plesae provide a stars"}
            return Response(render,status=status.HTTP_204_NO_CONTENT)


class RatingViewset(viewsets.ModelViewSet):
    queryset=Ratings.objects.all()
    serializer_class=RatingSerializer
    authentication_classes=(TokenAuthentication ,)
    permission_classes=(IsAuthenticated,)
