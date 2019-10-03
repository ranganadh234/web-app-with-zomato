from django.urls import path
from .views import bookings
urlpatterns=[
            path('form/',bookings,name='slots'),
            ]
