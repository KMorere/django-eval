from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

from .fields import DaysField


class Skill(models.Model):
    """
    A skill used by Users.
    """
    skill_name = models.CharField(max_length=100)

    def __str__(self):
        return self.skill_name


class Profile(models.Model):
    """
    A connected User profile.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    skills = models.ManyToManyField(Skill, related_name="skills")
    missing_skills = models.ManyToManyField(Skill, related_name="missing_skills")

    def __str__(self):
        return self.user.username + " " + [skill.__str__() for skill in self.skills.all()].__str__()


class Request(models.Model):
    """
    A Request created by a User at a schedule for a specific skill.
    """
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    schedule = DaysField()
    needed_skill = models.ForeignKey(Skill, on_delete=models.CASCADE)

    def __str__(self):
        return f"[{self.get_schedule_display()}] " + self.needed_skill.__str__() + f" Created by {self.author}."

    def get_request(self):
        return f"[{self.get_schedule_display().capitalize()}] " + self.needed_skill.__str__()


class Activity(models.Model):
    """
    An Activity between an 'active_user' helping the 'target_user'
    based on a 'request'.
    """
    activity_date = models.DateField()
    request = models.ForeignKey(Request, related_name="request", on_delete=models.CASCADE)
    helper = models.ForeignKey(Profile, related_name="helper", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "activity"
        verbose_name_plural = "activities"

    def __str__(self):
        return (f"[{self.activity_date}] - [{self.request.needed_skill}]" +
                f"\n\tHelper : {self.helper.user.username}.")

    @staticmethod
    def display_activities(request):
        if request is None or request == "None":
            return Activity.objects.all()
        return (Activity.objects.filter(activity_date__gte=timezone.now())
                .filter(request__needed_skill__skill_name=request))
