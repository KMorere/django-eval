from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

from .fields import DaysField


class Category(models.Model):
    """
    A category for skills.
    """
    category_name = models.CharField(max_length=100)

    class Meta:
        verbose_name = "category"
        verbose_name_plural = "categories"

    def __str__(self):
        return self.category_name


class Skill(models.Model):
    """
    A skill used by Users.
    """
    skill_name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True, default=None)

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

    def get_user(self):
        """
        Get the information of a user.
        """
        return self.user.first_name + " " + self.user.last_name + " - " + self.user.email


class Request(models.Model):
    """
    A Request created by a User at a schedule for a specific skill.
    """
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    schedule = DaysField()
    needed_skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    is_hidden = models.BooleanField()

    def __str__(self):
        return f"[{self.get_schedule_display()}] " + self.needed_skill.__str__() + f" Created by {self.author}."

    def get_request(self):
        """
        Display a request in a simple way with the schedule and needed skill.
        """
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

    def get_activity(self):
        """
        Display the activity in details.
        :return:
        """
        return (f"[{self.activity_date}] - [{self.request.needed_skill}]" +
                f"\n\tHelper : {self.helper.get_user()}.")

    @staticmethod
    def display_activities(request):
        """
        Get all the future activities.
        :param request: The requested skill to filter in the activities.
        :return: The filter activities in the database.
        """
        if request is None or request == "None":
            return Activity.objects.filter(activity_date__gte=timezone.now())
        return (Activity.objects.filter(activity_date__gte=timezone.now())
                .filter(request__needed_skill__skill_name=request))
