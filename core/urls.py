from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from api.views import *

router = routers.DefaultRouter()
router.register('users', UserViewSet, basename='Users')
router.register('livros', LivroViewSet, basename='Livros')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
