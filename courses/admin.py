from django.contrib import admin

from courses.models import Course, Lesson
from users.models import User


# Password 123
admin.site.register(Course)
admin.site.register(Lesson)
admin.site.register(User)

