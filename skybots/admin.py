from django.contrib import admin
from django.contrib.auth.models import Group
from .models import *
# Register your models here.
admin.site.register(AllMessage)
admin.site.register(Modules)
admin.site.register(Achievements)
admin.site.register(InteractiveButtons)
admin.site.register(Lessons)
admin.site.register(LessonsMessage)
admin.site.register(Quest)
admin.site.register(QuestMessage)
admin.site.register(QuestChoices)
admin.site.register(Themes)
admin.site.register(User)
admin.site.unregister(Group)


