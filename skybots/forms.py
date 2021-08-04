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
        model = User
        fields = ('username', 'password')


class CreateUserForms(forms.ModelForm):
    class Meta:
        model = User
        fields = ('full_name', 'email', 'phone_number', 'user_role', 'subscribe')

    subscribe = forms.DateTimeField(widget=forms.DateInput(attrs={'type': 'date'}))


class CreateThemesForms(forms.ModelForm):
    class Meta:
        model = Themes
        fields = ('themes_names', )


class CreateModuleForms(forms.ModelForm):
    class Meta:
        model = Modules
        fields = ('themes_id', 'module_name', 'module_description', 'module_photo')

    themes_id = forms.ModelChoiceField(queryset=Themes.objects.all())


class CreateLessonsForms(forms.ModelForm):
    class Meta:
        model = Lessons
        fields = ('id_modules', 'lessons_name', 'lessons_description', 'is_parent')
        id_modules = forms.ModelChoiceField(queryset=Modules.objects.all())


class CreateMessageLessonsForms(forms.ModelForm):
    MESSAGE_TYPE = (
        ("text", "Текст"),
        ("photo", "Фото"),
        ("video", "Видео"),
        ("doc", "Документ"),
    )

    class Meta:
        model = LessonsMessage
        fields = ('id_lessons','type_value', 'message_photos', 'message_caption', )

    id_lessons = forms.ModelChoiceField(queryset=Lessons.objects.all(), label="ID урока")
    type_value = forms.ChoiceField(choices=MESSAGE_TYPE, label="Тип сообщения")
    message_caption = forms.CharField(max_length=512, label="Подпись сообщения")
    message_photos = forms.FileField(label="Медиа-контент сообщения",required = False)
    message_value = forms.CharField(max_length=512, widget=forms.Textarea, label="Значение сообщения",required = False)


class CreateQuestForms(forms.ModelForm):
    class Meta:
        model = Quest
        fields = ('id_lessons', 'id_modules', 'quest_name', 'quest_description')

    id_lessons = forms.ModelChoiceField(queryset=Lessons.objects.all(), label="ID урока")
    id_modules = forms.ModelChoiceField(queryset=Modules.objects.all(), label="ID модуля")
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
        model = QuestMessage
        fields = ('quest_id', 'type_value', 'message_photos', 'message_value', 'message_caption')

    quest_id = forms.ModelChoiceField(queryset=Quest.objects.all(), label="ID квеста")
    type_value = forms.ChoiceField(choices=MESSAGE_TYPE, label="Тип сообщения")
    message_photos = forms.FileField(label="Медиа-контент сообщения",required = False)
    message_caption = forms.CharField(max_length=512, label="Подпись сообщения")
    message_value = forms.CharField(max_length=512, widget=forms.Textarea, label="Значение сообщения",required = False)


class CreateChoiceForQuestForms(forms.ModelForm):
    TRUE_CHOICE = (
        ('true', "Верно"),
        ("false", "Неверно"),
    )
    class Meta:
        model = QuestChoices
        fields = ('quest_id', 'choice_name', 'is_True', 'сhoice_description')
    quest_id = forms.ModelChoiceField(queryset=Quest.objects.all(), label="ID квеста")
    choice_name = forms.CharField(max_length=256, label="Имя выбора")
    is_true = forms.ChoiceField(choices=TRUE_CHOICE, label="Верность выбора")
    сhoice_description = forms.CharField(max_length=512, label="Описание выбора")


