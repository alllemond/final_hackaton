from django.db import router
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MovieViewSet, FavoriteView

router = DefaultRouter()

router.register('movie',MovieViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('saved/', FavoriteView.as_view())

]