from django.contrib import admin
from .models import User, Course, CourseContent, CourseMember, Comment

# Register your models here.
admin.site.register(Course)
admin.site.register(CourseContent)
admin.site.register(CourseMember)
admin.site.register(Comment)

