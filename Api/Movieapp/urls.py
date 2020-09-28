from django.contrib import admin
from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from .views import MovieViewset,RatingViewset,UserViewset
router=routers.DefaultRouter()
router.register('users',UserViewset)
router.register('movies',MovieViewset)
router.register('rating',RatingViewset)
urlpatterns = [
    path('', include(router.urls)),

]
