
from django.contrib import admin
from django.urls import path
from . import views

app_name = "studytool_app"

urlpatterns = [
    path("", views.home, name = "home"),
    path("course_index", views.course_index, name = "course_index"),
    path("major/<str:major_name>/", views.major, name = "major"),
    path("course/<str:course_name>/", views.course, name = "course"),
    path("search", views.search, name = "search"),
]
