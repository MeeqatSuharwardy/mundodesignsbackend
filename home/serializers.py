from rest_framework import serializers
from .models import About, Intro, Service


class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = '__all__'


class IntroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Intro
        fields = '__all__'


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'
