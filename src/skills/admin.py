from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import Activity, Profile, Skill


class ProfileInLine(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = "profiles"


class UserAdmin(BaseUserAdmin):
    inlines = [ProfileInLine]


class SkillAdmin(admin.ModelAdmin):
    list_display = ["skill_name"]


class ActivityAdmin(admin.ModelAdmin):
    list_display = ["activity_date", "needed_skill", "target_user", "active_user"]


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Skill, SkillAdmin)
admin.site.register(Activity, ActivityAdmin)
