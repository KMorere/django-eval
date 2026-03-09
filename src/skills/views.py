from django.shortcuts import render
from django.views import generic
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy

from .models import Profile


class HomeView(generic.ListView):
    template_name = "skills/home.html"
    context_object_name = "profiles"

    def get_queryset(self):
        return Profile.objects.all()
