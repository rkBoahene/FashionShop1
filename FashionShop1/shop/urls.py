from django.urls import path
from .views import welcomePage,login_page
urlpatterns = [
    path('mylogin/', login_page, name='mylogin'),
    path('', welcomePage, name='welcome')
]