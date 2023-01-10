from django.urls import path
from .views import HomeView, FanlarView, TurlarView

urlpatterns = [
    path('', HomeView, name='home'),
    path('fanlar/<int:pk>', FanlarView, name='fanlar'),
    path('tur/<int:pk>', TurlarView, name='turlar'),
]