from django.shortcuts import render

from rest_framework import viewsets

from .models import Language, Paradigm, Programmer
from .serializers import LanguageSerializer, ParadigmSerializer, ProgrammerSerializer

class ParadigmView(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = ParadigmSerializer


class LanguageView(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer


class ProgrammerView(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = ProgrammerSerializer