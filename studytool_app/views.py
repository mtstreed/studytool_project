from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Course, Major, Minor
from django.db.models import Q
from itertools import chain

# Create your views here.

def home(request):
    majors = Major.objects.order_by("name")
    context = {"majors": majors}
    return render(request, 'studytool_app/home.html', context)

def major(request, major_name):
    major = Major.objects.get(name = major_name)
    context = {"major": major}
    return render(request, 'studytool_app/major.html', context)

def course(request, course_name):
    course = Course.objects.get(name = course_name)
    context = {"course": course}
    return render(request, "studytool_app/course.html", context)

def course_index(request):
    courses = Course.objects.order_by("code")
    context = {"courses": courses}
    return render(request, "studytool_app/course_index.html", context)

def search(request):
    q = request.GET.get("q")
    course_results = Course.objects.filter(Q(name__icontains=q) | Q(code__icontains=q))
    major_results = Major.objects.filter(Q(name__icontains=q))
    #results = chain(course_results, major_results)
    majors = Major.objects.order_by("name")
    courses = Course.objects.order_by("code")
    #context = {"results": results, "majors": majors, "courses": courses}
    context = {"course_results": course_results, "major_results":major_results, "majors": majors, "courses": courses}
    return render(request, "studytool_app/search.html", context)
