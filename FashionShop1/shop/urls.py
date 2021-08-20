from django.urls import path
from .views import welcomePage
urlpatterns = [
    path('', welcomePage, name='welcome')
]