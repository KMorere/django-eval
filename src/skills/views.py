from django.shortcuts import render
from django.views import generic
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy

from .models import Activity, Profile, Skill


class HomeView(generic.ListView):
    model = Profile
    template_name = "skills/home.html"
    context_object_name = "profiles"
    extra_context = {
        "skills": "",
    }

    def get_queryset(self):
        return Activity.objects.filter(needed_skill__skill_name=self.request.GET.get("search", ""))


class SkillView(generic.ListView):
    model = Skill
    template_name = "skills/skills.html"
    context_object_name = "skills"

    def get_queryset(self):
        return Skill.objects.all().order_by("skill_name").values()
