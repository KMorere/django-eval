from django import forms

from .models import Skill, Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["skills", "missing_skills"]
        widgets = {
            "skills": forms.CheckboxSelectMultiple(),
            "missing_skills": forms.CheckboxSelectMultiple()
        }
