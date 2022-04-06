from django.shortcuts import render

# Create your views here.
from django.views.generic.edit import CreateView
from django.contrib.auth import get_user_model
User = get_user_model()
from django.urls import reverse_lazy
from accounts.forms import *


# @method_decorator(login_required, name='dispatch')
class ProfileCreation(CreateView):
    model = User
    form_class =UserCreatedForm
    success_url = reverse_lazy('accounts:profile')
    template_name = 'registration/editProfile.html'  # a list of all posts will be displayed on index.html
    context_object_name = 'form'
# Mohan10sunka@
