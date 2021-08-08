from django.contrib import admin
from django.contrib.auth.models import Group
from .models import *
# Register your models here.
admin.site.register(skybots_allmessage)
admin.site.register(skybots_modules)
admin.site.register(skybots_achievements)
admin.site.register(skybots_interactivebuttons)
admin.site.register(skybots_lessons)
admin.site.register(skybots_lessonsmessage)
admin.site.register(skybots_quest)
admin.site.register(skybots_questmessage)
admin.site.register(skybots_questchoices)
admin.site.register(skybots_themes)
admin.site.register(skybots_user)
admin.site.unregister(Group)


