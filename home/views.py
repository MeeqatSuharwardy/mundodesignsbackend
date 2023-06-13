from django.shortcuts import render

# Create your views here.
from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.response import Response
from .models import About, Intro, Service
from .serializers import AboutSerializer, IntroSerializer, ServiceSerializer


class AboutView(generics.RetrieveAPIView):
    queryset = About.objects.all()
    serializer_class = AboutSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = get_object_or_404(self.get_queryset())
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class IntroView(generics.ListAPIView):
    queryset = Intro.objects.all()
    serializer_class = IntroSerializer


class ServiceView(generics.ListAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
