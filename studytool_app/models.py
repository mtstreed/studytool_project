from django.db import models

# Create your models here.

class Course(models.Model):
    name = models.CharField(max_length = 200)
    code = models.CharField(max_length = 200)
    coordinator = models.CharField(max_length = 200, blank = True)
    euc_coordinator = models.CharField(max_length = 200)
    euc_coordinator_email = models.EmailField(max_length = 100,  blank = True)
    prereqs = models.CharField(max_length = 3000, blank = True)
    level = models.IntegerField()
    quad = models.IntegerField()
    blurb = models.CharField(max_length = 3000, blank = True)
    note = models.CharField(max_length = 3000, blank = True)
    def __str__(self):
        return self.name


class Major(models.Model):
    name = models.CharField(max_length = 200)
    courses_mandatory = models.ManyToManyField(Course)
    num_selected = models.IntegerField(null = True, blank = True)
    courses_selected = models.ManyToManyField(Course, related_name = "selected", null = True, blank = True)
    note = models.CharField(max_length = 3000, blank = True)
    def __str__(self):
        return self.name


class Minor(models.Model):
    name = models.CharField(max_length = 200)
    courses = models.ManyToManyField(Course)
    note = models.CharField(max_length = 3000, blank = True)
    def __str__(self):
        return self.name
