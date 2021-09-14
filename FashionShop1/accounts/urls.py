from django.urls import path
from .views import login_page, register_page

app_name = 'accounts'
urlpatterns = [
    path('mylogin/', login_page, name='login'),
    path('myregister/', register_page, name='register'),
    
]