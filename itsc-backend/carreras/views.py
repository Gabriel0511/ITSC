from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet
from .models import Carrera
from .serializers import CarreraSerializer

class CarreraViewSet(ModelViewSet):
    queryset = Carrera.objects.all()
    serializer_class = CarreraSerializer