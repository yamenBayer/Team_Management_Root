import imp
from django.contrib import admin
from .models import Message, Notification, Profile, Project, Task, Team, Team_Request

admin.site.register(Task)
admin.site.register(Project)
admin.site.register(Team)
admin.site.register(Profile)
admin.site.register(Team_Request)
admin.site.register(Message)
admin.site.register(Notification)
