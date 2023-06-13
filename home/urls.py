from django.urls import path
from . import views

urlpatterns = [
    path('about/', views.AboutView.as_view(), name='about-api'),
    path('intro/', views.IntroView.as_view(), name='intro-api'),
    path('services/', views.ServiceView.as_view(), name='services-api'),
]
