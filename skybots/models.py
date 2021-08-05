import os
import uuid


from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _


# Create your models here.


def get_upload_path(instance, filename):
    return 'original_image/{uuid}/{filename}'.format(uuid=uuid.uuid4().hex, filename=filename)


class AllMessage(models.Model):
    MESSAGE_TYPE = (
        ("text", "Текст"),
        ("photo", "Фото"),
        ("video", "Видео"),
        ("doc", "Документ"),
    )

    message_type = models.CharField(max_length=255, choices=MESSAGE_TYPE, null=True, verbose_name="Тип сообщения")
    message_caption = models.TextField(max_length=255, blank=True, null=True, verbose_name="Подпись под контент")
    message_photos = models.FileField(upload_to=get_upload_path, blank=True, null=True)

    class Meta:
        verbose_name = "Сообщение"
        verbose_name_plural = "База сообщений"

    def __str__(self):
        return "Сообщение № {}".format(self.pk)


class Themes(models.Model):
    themes_names = models.CharField(max_length=256, verbose_name="Имя темы", unique=True)

    class Meta:
        verbose_name = "Тема"
        verbose_name_plural = "База тем"

    def __str__(self):
        return self.themes_names


class Modules(models.Model):
    themes_id = models.ForeignKey(Themes, on_delete=models.CASCADE, default=True, null=True, verbose_name="ID темы")
    module_name = models.CharField(max_length=256, verbose_name="Имя модуля", unique=True)
    module_description = models.TextField(blank=True, null=True, verbose_name="Описание модуля")
    module_photo = models.ImageField(upload_to=get_upload_path, default=True, verbose_name="Фото модуля")
    module_video = models.FileField(upload_to=get_upload_path, blank=True, verbose_name="Видео модуля")
    data_create_module = models.DateTimeField(auto_now=True, verbose_name="Дата создания модуля")

    class Meta:
        verbose_name = "Модуль"
        verbose_name_plural = "База модулей"

    def __str__(self):
        return self.module_name


class Lessons(models.Model):
    PARENTS = (
        (0, "Ребенок"),
        (1, "Родитель"),
        (2, "Для всех"),
    )

    VERSION_LES = (
        (0, "Краткая версия"),
        (1, "Полная версия"),
    )

    id_modules = models.ForeignKey(Modules, related_name="lessonsformoule", on_delete=models.CASCADE, verbose_name="ID модуля")
    lessons_name = models.CharField(max_length=256, verbose_name="Название урока")
    lessons_description = models.TextField(blank=True, null=True, verbose_name="Описание урока")
    is_parent = models.IntegerField(choices=PARENTS, null=True, verbose_name="Тип урока")
    is_short = models.IntegerField(choices=VERSION_LES, null=True, verbose_name="Версия урока")
    data_create_lessons = models.DateTimeField(auto_now=True, verbose_name="Дата создания урока")

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "База уроков"

    def __str__(self):
        return self.lessons_name


class LessonsMessage(models.Model):
    id_lessons = models.ForeignKey(Lessons, on_delete=models.CASCADE, verbose_name="ID урока")
    id_AllMessages = models.ForeignKey(AllMessage, on_delete=models.CASCADE, verbose_name="ID сообщения")

    class Meta:
        verbose_name = "Сообщения урока"
        verbose_name_plural = "База сообщений для уроков"

    def __str__(self):
        return "Сообщение № {} для урока {}".format(self.id_AllMessages.pk, self.id_lessons.lessons_name)


class Vocabulary(models.Model):
    id_lessons = models.ForeignKey(Lessons, on_delete=models.CASCADE, verbose_name="ID урока")
    message_id = models.ForeignKey(AllMessage, on_delete=models.CASCADE, verbose_name="ID сообщения")

    class Meta:
        verbose_name = "Словарь"
        verbose_name_plural = "База словарей"

    def __str__(self):
        return "Сообщение № {} для урока {}".format(self.message_id.pk, self.id_lessons.lessons_name)


class Quest(models.Model):
    IS_HARD = (
        (0, "Легко"),
        (1, "Сложно")
    )
    id_modules = models.ForeignKey(Modules, on_delete=models.CASCADE, verbose_name="ID модуля")
    id_lessons = models.ForeignKey(Lessons, on_delete=models.CASCADE, verbose_name="ID урока")
    quest_name = models.CharField(max_length=1024, verbose_name="Название квеста", unique=True)
    quest_description = models.TextField(blank=True, null=True, verbose_name="Описание квеста")
    data_create_quest = models.DateTimeField(auto_now=True, verbose_name="Дата создания квеста")
    is_hard = models.CharField(max_length=255, null=True, choices=IS_HARD, verbose_name="Сложность вопроса")

    class Meta:
        verbose_name = "Квест"
        verbose_name_plural = "База квестов"

    def __str__(self):
        return self.quest_name


class QuestMessage(models.Model):
    quest_id = models.ForeignKey(Quest, on_delete=models.CASCADE, verbose_name="ID квеста")
    id_AllMessages = models.ForeignKey(AllMessage, on_delete=models.CASCADE, verbose_name="ID сообщения")

    class Meta:
        verbose_name = "Сообщение квестов"
        verbose_name_plural = "База сообщений для квестов"

    def __str__(self):
        return "Сообщение № {} для квеста {}".format(self.id_AllMessages.pk, self.quest_id.quest_name)


class QuestChoices(models.Model):
    TRUE_CHOICE = (
        ('true', "Верно"),
        ("false", "Неверно"),
    )

    quest_id = models.ForeignKey(Quest, on_delete=models.CASCADE, verbose_name="ID квеста")
    choice_name = models.CharField(max_length=128, verbose_name="Названия выбора")
    сhoice_description = models.CharField(max_length=512, blank=True, null=True, verbose_name="Описание выбора ответа")
    is_True = models.CharField(max_length=255, choices=TRUE_CHOICE,  null=True, verbose_name="Правильность выбора")

    class Meta:
        verbose_name = "Ответ для квестов"
        verbose_name_plural = "База ответов для квестов"

    def __str__(self):
        return "Выбор {}({}) - для квеста {}".format(self.choice_name, self.is_True, self.quest_id.quest_name)


class Achievements(models.Model):
    lesson_id = models.ForeignKey(Lessons, on_delete=models.CASCADE, verbose_name="ID урока")
    achieve_name = models.CharField(max_length=255, verbose_name="Название ачивки")
    achieve_description = models.TextField(blank=True, null=True, verbose_name="Описание ачивки")
    achieve_photo = models.ImageField(upload_to=get_upload_path, default=True, verbose_name="Фото ачивки")

    class Meta:
        verbose_name = "Ачивки"
        verbose_name_plural = "База ачивок"

    def __str__(self):
        return self.achieve_name


class User(AbstractUser):
    CONFIRM_TYPE = (
        (0, 0),
        (1, 1),
    )

    USER_ROLE = (
        ("parent", "Родитель"),
        ("children", "Ребенок"),
    )
    user_id = models.CharField(max_length=256, verbose_name="ID пользователя")
    date_reg = models.DateTimeField(auto_now=True, verbose_name="Дата регестрации")
    first_name = models.CharField(max_length=256, verbose_name="Имя пользователя")
    last_name = models.CharField(max_length=256, verbose_name="Фамилия пользователя")
    full_name = models.CharField(max_length=512, verbose_name="Полное имя")
    phone_number = models.CharField(max_length=20, verbose_name="Номер телефона")
    username = models.CharField(max_length=50, blank=True, null=True, unique=True, verbose_name="Логин пользователя")
    email = models.EmailField(_('email address'), unique=True)
    is_confirm = models.IntegerField(choices=CONFIRM_TYPE, null=True, verbose_name="Статус подтверждения")
    user_role = models.CharField(max_length=256, choices=USER_ROLE, verbose_name="Роль пользователя")
    is_live = models.IntegerField(choices=CONFIRM_TYPE, null=True, verbose_name="Активность пользователя")
    subscribe = models.DateTimeField(null=True, blank=True, verbose_name="Дата подписки пользователя")
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "База пользователей"

    def __str__(self):
        return "{}".format(self.email)



