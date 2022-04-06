from django.contrib import admin
from .models import Question, Answer, User
from django.contrib.auth.admin import UserAdmin

admin.site.register(User, UserAdmin)
admin.site.register(Question)
admin.site.register(Answer)
