from django.shortcuts import render
from django.views.generic.edit import CreateView

from . forms import CustomUserCreationForm


class SignUpView(CreateView):
    form_class = CustomUserCreationForm

