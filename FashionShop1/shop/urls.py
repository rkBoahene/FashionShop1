from django.urls import path
from .views import login_page, register_page
urlpatterns = [
    path('mylogin/', login_page, name='mylogin'),
    path('myregister/', register_page, name='myregister'),
    
]