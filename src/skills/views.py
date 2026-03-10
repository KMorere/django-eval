from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.db.models import Q

from .models import Activity, Profile, Skill
from .forms import ProfileForm


class HomeView(generic.ListView):
    model = Activity
    template_name = "skills/home.html"
    context_object_name = "profiles"
    extra_context = {
        "skills": Skill.objects.all(),
    }

    def get_queryset(self):
        return self.model.display_activities(self.request.GET.get("search", None))


class SkillView(generic.ListView):
    model = Skill
    template_name = "skills/skills.html"
    context_object_name = "skills"

    def get_queryset(self):
        return Skill.objects.all().order_by("skill_name").values()


def profile(request, pk):
    pf = get_object_or_404(Profile, pk=pk)
    if request.method == "POST":
        form = ProfileForm(request.POST, instance=pf)

        if form.is_valid():
            pf_form = form.save(commit=False)
            new_skill = form.cleaned_data["skills"]
            pf.skills.set(new_skill)
            pf_form.save()

            return HttpResponseRedirect(reverse("skills:profile", args=(pk,)))
    else:
        form = ProfileForm(instance=pf)

    return render(request, "skills/profile.html", {
        "skills": Profile.objects.get(pk=pk).skills.all(),
        "activities": Activity.objects.filter(Q(target_user__pk=pk) | Q(active_user__pk=pk)),
        "form": form
    })
