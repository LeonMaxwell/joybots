from django import forms
from django.core.exceptions import NON_FIELD_ERRORS

from .models import *


class LoginUserForms(forms.ModelForm):
    username = forms.CharField(max_length=255, label="Username")
    password = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        help_text="",)

    class Meta:
        model = skybots_user
        fields = ('username', 'password')


class CreateUserForms(forms.ModelForm):
    class Meta:
        model = skybots_user
        fields = ('user_id', 'full_name', 'email', 'phone_number', 'user_role', 'subscribe')

    subscribe = forms.DateTimeField(widget=forms.DateInput(attrs={'type': 'date'}), label="Подписка")


class CreateThemesForms(forms.ModelForm):
    class Meta:
        model = skybots_themes
        fields = ('themes_names', )


class CreateModuleForms(forms.ModelForm):
    class Meta:
        model = skybots_modules
        fields = ('themes_id', 'module_name', 'module_description', 'module_photo', 'module_video')

    themes_id = forms.ModelChoiceField(queryset=skybots_themes.objects.all(), label="ID темы")


class CreateLessonsForms(forms.ModelForm):
    class Meta:
        model = skybots_lessons
        fields = ('id_modules', 'is_short', 'is_parent', 'lessons_name', 'lessons_description')
    id_modules = forms.ModelChoiceField(queryset=skybots_modules.objects.all(), label="ID модуля")


class CreateMessageLessonsForms(forms.ModelForm):
    MESSAGE_TYPE = (
        ("text", "Текст"),
        ("photo", "Фото"),
        ("video", "Видео"),
        ("doc", "Документ"),
    )

    class Meta:
        model = skybots_lessonsmessage
        fields = ('id_lessons','type_value', 'message_photos', 'message_caption', )

    id_lessons = forms.ModelChoiceField(queryset=skybots_lessons.objects.all(), label="ID урока")
    type_value = forms.ChoiceField(choices=MESSAGE_TYPE, label="Тип сообщения")
    message_caption = forms.CharField(max_length=512, widget=forms.Textarea, label="Подпись сообщения",required = False)
    message_photos = forms.FileField(label="Медиа-контент сообщения",required = False)


class CreateVocabularyForms(forms.ModelForm):
    MESSAGE_TYPE = (
        ("text", "Текст"),
        ("photo", "Фото"),
        ("video", "Видео"),
        ("doc", "Документ"),
    )

    class Meta:
        model = skybots_vocabulary
        fields = ('id_lessons','type_value', 'message_photos', 'message_caption')

    id_lessons = forms.ModelChoiceField(queryset=skybots_lessons.objects.all(), label="ID урока")
    type_value = forms.ChoiceField(choices=MESSAGE_TYPE, label="Тип сообщения")
    message_caption = forms.CharField(max_length=512, widget=forms.Textarea, label="Подпись сообщения",required = False)
    message_photos = forms.FileField(label="Медиа-контент сообщения",required = False)


class CreateQuestForms(forms.ModelForm):
    class Meta:
        model = skybots_quest
        fields = ('id_modules', 'id_lessons', 'quest_name', 'is_hard', 'quest_description')

    id_modules = forms.ModelChoiceField(queryset=skybots_modules.objects.all(), label="ID модуля")
    id_lessons = forms.ModelChoiceField(queryset=skybots_lessons.objects.all(), label="ID урока")
    quest_name = forms.CharField(max_length=256, label="Название квеста")
    quest_description = forms.CharField(widget=forms.Textarea, label="Описание квеста")


class CreateMessageForQuestForms(forms.ModelForm):
    MESSAGE_TYPE = (
        ("text", "Текст"),
        ("photo", "Фото"),
        ("video", "Видео"),
        ("doc", "Документ"),
    )

    class Meta:
        model = skybots_questmessage
        fields = ('quest_id', 'type_value', 'message_photos', 'message_caption')

    quest_id = forms.ModelChoiceField(queryset=skybots_quest.objects.all(), label="ID квеста")
    type_value = forms.ChoiceField(choices=MESSAGE_TYPE, label="Тип сообщения")
    message_photos = forms.FileField(label="Медиа-контент сообщения",required = False)
    message_caption = forms.CharField(max_length=512,  widget=forms.Textarea, required = False, label="Подпись сообщения")


class CreateChoiceForQuestForms(forms.ModelForm):
    TRUE_CHOICE = (
        ('true', "Верно"),
        ("false", "Неверно"),
    )

    class Meta:
        model = skybots_questchoices
        fields = ('quest_id', 'choice_name', 'is_True', 'сhoice_description')
    quest_id = forms.ModelChoiceField(queryset=skybots_quest.objects.all(), label="ID квеста")
    choice_name = forms.CharField(max_length=256, label="Имя выбора")
    is_True = forms.ChoiceField(choices=TRUE_CHOICE, label="Верность выбора")
    сhoice_description = forms.CharField(max_length=512, label="Описание выбора")


class CreateAchievementsForms(forms.ModelForm):
    class Meta:
        model = skybots_achievements
        fields = ('lesson_id', 'achieve_name', 'achieve_description', 'achieve_photo')
    lesson_id = forms.ModelChoiceField(queryset=skybots_lessons.objects.all(), label="ID урока")


class CreateInteractiveButtonsForms(forms.ModelForm):
    class Meta:
        model = skybots_interactivebuttons
        fields = ('module_id', 'lessons_id', 'button_name', 'message_id', 'achieve_id')