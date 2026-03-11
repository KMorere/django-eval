from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.db.models import Q
from django.utils import timezone

from .models import Activity, Profile, Request, Skill
from .forms import ProfileForm, RequestForm, ActivityForm, SearchForm


def home(request):
    """
    View of the homepage.
    """
    categories = SearchForm
    search_query = request.GET.get("skills", None)
    if request.user.is_authenticated:
        requests = (Request.objects.filter(
            needed_skill__skill_name=Skill.objects.get(pk=request.user.pk).skill_name)
                    .exclude(is_hidden=True)
                    .filter(needed_skill__skill_name=search_query))
    else:
        requests = None

    if request.method == "POST":
        form = ActivityForm(request.POST)

        if form.is_valid():
            a_id = form.cleaned_data["request_id"]
            req = get_object_or_404(Request, id=a_id)
            Activity.objects.create(
                activity_date=timezone.now(),
                request=req,
                helper=Profile.objects.get(pk=request.user.pk)
            )
            req.is_hidden = True
            req.save()

            return HttpResponseRedirect(reverse("skills:home"))
    else:
        form = ActivityForm

    return render(request, "skills/home.html", {
        "activities": Activity.display_activities(search_query),
        "skills": Skill.objects.all(),
        "requests": requests,
        "form": form,
        "categories": categories
    })


class SkillView(generic.ListView):
    """
    View of all skills.
    """
    model = Skill
    template_name = "skills/skills.html"
    context_object_name = "skills"

    def get_queryset(self):
        return Skill.objects.all().order_by("skill_name").values()


@login_required
def profile(request, pk):
    """
    View of the currently connected user's profile
    """
    pf = get_object_or_404(Profile, pk=pk)

    if pf.user != request.user:
        return HttpResponseRedirect(reverse("skills:home"))

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
        "activities": Activity.objects.filter(Q(request__author__pk=pk) | Q(helper__pk=pk)),
        "form": form,
    })


@login_required
def request_form(request):
    """
    View of the request creation for the current user.
    """
    if request.method == "POST":
        form = RequestForm(request.POST)

        if form.is_valid():
            req_form = form.save(commit=False)
            days = form.cleaned_data["schedule"]
            req_form.days = days
            req_form.author = Profile.objects.get(pk=request.user.pk)
            req_form.save()

            return HttpResponseRedirect(reverse("skills:home"))
    else:
        form = RequestForm()
        form.fields["needed_skill"].queryset = Profile.objects.get(pk=request.user.pk).missing_skills

    return render(request, "skills/request.html", {
        "requests": Request.objects.all(),
        "form": form,
    })
