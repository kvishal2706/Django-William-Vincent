from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import TemplateView

class SignUpView(generic.CreateView):
    form_class=UserCreationForm
    success_url=reverse_lazy('login')
    template_name='registration/signup.html'

class LogOutView(TemplateView):
    template_name='registration/logout.html'
    success_url=reverse_lazy('home')


# Create your views here.
