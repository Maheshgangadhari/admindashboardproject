from django.urls import path
from accounts.views import *

app_name='accounts'
urlpatterns = [
    # profile
    path('profile/',ProfileCreation.as_view(),name='profile'),

]
