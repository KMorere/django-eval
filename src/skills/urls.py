from django.urls import path
from . import views

app_name = "skills"
urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("all/", views.SkillView.as_view(), name="all"),
    path("profile/<int:pk>/", views.profile, name="profile"),
    path("request/", views.request_form, name="request"),
]
