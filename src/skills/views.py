from django.shortcuts import render
from django.views import generic
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy

from .models import Profile, Skill


class HomeView(generic.ListView):
    model = Profile
    template_name = "skills/home.html"
    context_object_name = "profiles"

    def get_queryset(self):
        return Profile.objects.all()


class SkillView(generic.ListView):
    model = Skill
    template_name = "skills/skills.html"
    context_object_name = "skills"

    def get_queryset(self):
        return Skill.objects.all().order_by("skill_name").values()
