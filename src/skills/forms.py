from django import forms
from django.utils.translation import gettext as _

from .models import Activity, Profile, Request, Skill


class ProfileForm(forms.ModelForm):
    """
    Form in the profile view to modify the current user's skills.
    """
    class Meta:
        model = Profile
        fields = ["skills", "missing_skills"]
        widgets = {
            "skills": forms.CheckboxSelectMultiple(),
            "missing_skills": forms.CheckboxSelectMultiple()
        }


DAYS = {
    '1': _(u'Monday'),
    '2': _(u'Tuesday'),
    '3': _(u'Wednesday'),
    '4': _(u'Thursday'),
    '5': _(u'Friday'),
    '6': _(u'Saturday'),
    '7': _(u'Sunday')
}


class RequestForm(forms.ModelForm):
    """
    Creation of a request.
    """
    schedule = forms.ChoiceField(
        choices=[(key, value) for key, value in DAYS.items()],
        required=True,
        widget=forms.Select(attrs={"class": "form-control"})
    )

    needed_skill = forms.ModelChoiceField(
        queryset=Skill.objects.all(),
        required=True,
        widget=forms.Select(attrs={"class": "form-control"})
    )

    class Meta:
        model = Request
        fields = ["schedule", "needed_skill"]


class ActivityForm(forms.Form):
    """
    Hidden form to accept a request.
    """
    request_id = forms.IntegerField(widget=forms.HiddenInput())
