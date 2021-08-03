import datetime

import xlwt
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LogoutView
from django.http import HttpResponse
from django.shortcuts import render
from django.template import RequestContext
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_protect
from pip._internal.operations.install.wheel import req_error_context
from .forms import *
from .forms import LoginUserForms
from .models import User
# Create your views here.
from .models import *
from django.views.generic import TemplateView, FormView, CreateView
# from skybotsPanel.settings import connection
# import mysql.connector
# from mysql.connector import Error
# from skybotsPanel.settings import db_confg


# def create_connection_mysql_db(db_host, db_name, user_name, user_password):
#     connection_db = None
#     try:
#         connection_db = mysql.connector.connect(
#             host=db_host,
#             user=user_name,
#             password=user_password,
#             database=db_name,
#         )
#         print("Пдключение к MySQL успешно выполнено")
#     except Error as db_connection_error:
#         print("Возникла ошибка: ", db_connection_error)
#     return connection_db


# conn = create_connection_mysql_db(db_confg["mysql"]["host"],
#                                   db_confg["mysql"]["db_name"],
#                                   db_confg["mysql"]["user"],
#                                   db_confg["mysql"]["pass"])


class LoginUser(FormView):
    template_name = "elements/login.html"
    form_class = LoginUserForms

    def get(self, request, *args, **kwargs):
        userData = User.objects.all()
        allMessagesData = AllMessage.objects.all()
        modulesData = Modules.objects.all()
        quest = Quest.objects.all()
        questData = QuestMessage.objects.all()
        lessons = Lessons.objects.all()
        lessonsData = LessonsMessage.objects.all()
        user_is = request.user
        if user_is.is_authenticated:
            return render(request, 'index.html', {"it_user": user_is,
                                                  "userData": userData,
                                                  "allMessagesData": allMessagesData,
                                                  "modulesData": modulesData,
                                                  "quest": quest,
                                                  "questData": questData,
                                                  "lessons": lessons,
                                                  "lessonsData": lessonsData, })
        else:
            return render(request, self.template_name, {'form': self.form_class, 'act': 'login'})

    def post(self, request, *args, **kwargs):
        form = LoginUserForms(request.POST)
        username = form['username'].data
        password = form['password'].data
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                user_is = request.user
                return render(request, 'index.html', {"it_user": user_is})
            else:
                return render(request, 'elements/login.html')
        else:
            return render(request, 'index.html')


class PartsView(CreateView):

    def get(self, request, *args, **kwargs):
        data_for_table = 0
        type_cont = kwargs['name_parts']
        if type_cont == 'users':
            data_for_table = User.objects.all()
        elif type_cont == 'modules':
            data_for_table = Modules.objects.all()
        elif type_cont == 'lessons':
            data_for_table = Lessons.objects.all()
        elif type_cont == 'allMessages':
            data_for_table = AllMessage.objects.all()
        elif type_cont == 'msglessons':
            data_for_table = LessonsMessage.objects.all()
        elif type_cont == 'quests':
            data_for_table = Quest.objects.all()
        elif type_cont == 'msgquests':
            data_for_table = QuestMessage.objects.all()
        elif type_cont == 'choicequests':
            data_for_table = QuestChoices.objects.all()
        user_is = request.user
        return render(request, 'elements/input.html', {
            "type": type_cont,
            "it_user": user_is,
            "date": data_for_table, })


class CreateModels(CreateView):
    form_class = CreateUserForms
    model = User
    template_name = 'forms/forms_user.html'
    success_url = reverse_lazy('login')

    def get(self, request, *args, **kwargs):
        type_cont = kwargs['name_parts']
        user_is = request.user
        if type_cont == 'users':
            self.form_class = CreateUserForms
            self.model = User
            self.template_name = 'forms/forms_user.html'
        elif type_cont == 'modules':
            self.form_class = CreateModuleForms
            self.model = Modules
            self.template_name = 'forms/forms_modules.html'
        elif type_cont == 'lessons':
            self.form_class = CreateLessonsForms
            self.model = Lessons
            self.template_name = 'forms/forms_lessons.html'
        elif type_cont == 'msglessons':
            self.form_class = CreateMessageLessonsForms
            self.model = LessonsMessage
            self.template_name = 'forms/forms_lessonsmsg.html'
        elif type_cont == 'quests':
            self.form_class = CreateQuestForms
            self.model = Quest
            self.template_name = 'forms/form_quest.html'
        elif type_cont == 'msgquests':
            self.form_class = CreateMessageForQuestForms
            self.model = QuestMessage
            self.template_name = 'forms/form_questmsg.html'
        elif type_cont == 'choicequests':
            self.form_class = CreateChoiceForQuestForms
            self.model = QuestChoices
            self.template_name = 'forms/form_questchoice.html'
        return render(request, self.template_name, {'form': self.form_class, "it_user": user_is})


class EditModels(CreateView):
    form_class = CreateUserForms
    model = User
    template_name = 'forms/forms_user_edit.html'
    success_url = reverse_lazy('login')

    def get(self, request, *args, **kwargs):
        type_cont = kwargs['name_parts']
        pk_cont = kwargs['pk']
        user_is = request.user
        if type_cont == 'users':
            self.form_class = CreateUserForms
            self.model = User
            self.template_name = 'forms/forms_user_edit.html'
        elif type_cont == 'modules':
            self.form_class = CreateModuleForms
            self.model = Modules
            self.template_name = 'forms/forms_modules_edit.html'
        elif type_cont == 'lessons':
            self.form_class = CreateLessonsForms
            self.model = Lessons
            self.template_name = 'forms/forms_lessons_edit.html'
        elif type_cont == 'msglessons':
            self.form_class = CreateMessageLessonsForms
            self.model = LessonsMessage
            self.template_name = 'forms/forms_lessonsmsg.html'
        elif type_cont == 'quests':
            self.form_class = CreateQuestForms
            self.model = Quest
            self.template_name = 'forms/form_quest.html'
        elif type_cont == 'msgquests':
            self.form_class = CreateMessageForQuestForms
            self.model = QuestMessage
            self.template_name = 'forms/form_questmsg.html'
        elif type_cont == 'choicequests':
            self.form_class = CreateChoiceForQuestForms
            self.model = QuestChoices
            self.template_name = 'forms/form_questchoice.html'
        return render(request, self.template_name, {'form': self.form_class, 'pk': pk_cont, "it_user": user_is})


def userDelete(request, name_parts, pk):
#    cursor = conn.cursor()
    user_is = request.user
    try:
        model = User.objects.get(id=pk)
        # userDelete_pk = '{}'.format(pk)
        # insert_quesy_to_table = '''
        # delete from user where user_pk='{}';''' \
        #     .format(userDelete_pk)
        # cursor.execute(insert_quesy_to_table)
        # conn.commit()
        model.delete()
        return render(request, 'index.html', {"it_user": user_is})
    except User.DoesNotExist:
        return render(request, 'index.html', {"it_user": user_is})


def moduleDelete(request, name_parts, pk):
    user_is = request.user
#    cursor = conn.cursor()
    try:
        model = Modules.objects.get(id=pk)
        # userDelete_pk = '{}'.format(pk)
        # insert_quesy_to_table = '''
        # delete from modules where module_id='{}';''' \
        #     .format(userDelete_pk)
        # cursor.execute(insert_quesy_to_table)
        # conn.commit()
        model.delete()
        return render(request, 'index.html', {"it_user": user_is})
    except User.DoesNotExist:
        return render(request, 'index.html', {"it_user": user_is})


def lessonsDelete(request, name_parts, pk):
#    cursor = conn.cursor()
    user_is = request.user
    try:
        model = Lessons.objects.get(id=pk)
        # userDelete_pk = '{}'.format(pk)
        # insert_quesy_to_table = '''
        # delete from lessons where lesson_id='{}';''' \
        #     .format(userDelete_pk)
        # cursor.execute(insert_quesy_to_table)
        # conn.commit()
        model.delete()
        return render(request, 'index.html', {"it_user": user_is})
    except User.DoesNotExist:
        return render(request, 'index.html', {"it_user": user_is})


def lessonsmsgDelete(request, name_parts, pk):
  #  cursor = conn.cursor()
    user_is = request.user
    try:
        model = LessonsMessage.objects.get(id=pk)
        # userDelete_pk = '{}'.format(pk)
        # insert_quesy_to_table = '''
        # delete from lessons_messages where id='{}';''' \
        #     .format(userDelete_pk)
        # cursor.execute(insert_quesy_to_table)
        # conn.commit()
        model.delete()
        return render(request, 'index.html', {"it_user": user_is})
    except User.DoesNotExist:
        return render(request, 'index.html', {"it_user": user_is})


def questsDelete(request, name_parts, pk):
 #   cursor = conn.cursor()
    user_is = request.user
    try:
        model = Quest.objects.get(id=pk)
        # userDelete_pk = '{}'.format(pk)
        # insert_quesy_to_table = '''
        # delete from quests where quest_id='{}';''' \
        #     .format(userDelete_pk)
        # cursor.execute(insert_quesy_to_table)
        # conn.commit()
        model.delete()
        return render(request, 'index.html', {"it_user": user_is})
    except User.DoesNotExist:
        return render(request, 'index.html', {"it_user": user_is})


def questsmsgDelete(request, name_parts, pk):
#    cursor = conn.cursor()
    user_is = request.user
    try:
        model = QuestMessage.objects.get(id=pk)
        # userDelete_pk = '{}'.format(pk)
        # insert_quesy_to_table = '''
        # delete from quests_messages where id='{}';''' \
        #     .format(userDelete_pk)
        # cursor.execute(insert_quesy_to_table)
        # conn.commit()
        model.delete()
        return render(request, 'index.html', {"it_user": user_is})
    except User.DoesNotExist:
        return render(request, 'index.html', {"it_user": user_is})


def questschoiceDelete(request, name_parts, pk):
#    cursor = conn.cursor()
    user_is = request.user
    try:
        model = QuestChoices.objects.get(id=pk)
        # userDelete_pk = '{}'.format(pk)
        # insert_quesy_to_table = '''
        # delete from quests_choices where choice_id='{}';''' \
        #     .format(userDelete_pk)
        # cursor.execute(insert_quesy_to_table)
        # conn.commit()
        model.delete()
        return render(request, 'index.html', {"it_user": user_is})
    except User.DoesNotExist:
        return render(request, 'index.html', {"it_user": user_is})


def userEdit(request, name_parts, pk):
#    cursor = conn.cursor()
    user_is = request.user
    try:
        form = CreateUserForms
        user = User.objects.get(id=pk)

        if request.method == "POST":
            userEdit_pk = '{}'.format(pk)
            user.full_name = request.POST.get("full_name")
            userEdit_full_name = '{}'.format(request.POST.get("full_name"))
            user.email = request.POST.get("email")
            userEditEmail = '{}'.format(request.POST.get("email"))
            user.phone_number = request.POST.get("phone_number")
            userEditPhone_number = '{}'.format(request.POST.get("phone_number"))
            user.user_role = request.POST.get("user_role")
            userEdit_user_role = '{}'.format(request.POST.get("user_role"))
            # insert_quesy_to_table = '''
            # update user set full_name='{}', phone_number='{}', email='{}', user_role='{}' where user_pk='{}';'''\
            #     .format(userEdit_full_name, userEditPhone_number,userEditEmail,userEdit_user_role, userEdit_pk)
            # cursor.execute(insert_quesy_to_table)
            # conn.commit()
            user.save()
            return render(request, 'index.html', {"it_user": user_is})
        else:
            return render(request, 'forms/forms_user_edit.html',
                          {"pk": pk, "object": user, 'form': form, "it_user": user_is})
    except User.DoesNotExist:
        return render(request, 'index.html', {"it_user": user_is})


def moduleEdit(request, name_parts, pk):
#    cursor = conn.cursor()
    user_is = request.user
    try:
        form = CreateModuleForms
        module = Modules.objects.get(id=pk)

        if request.method == "POST":
            userEdit_pk = '{}'.format(pk)
            module.module_name = request.POST.get("module_name")
            moduleEdit_module_name = '{}'.format(request.POST.get("module_name"))
            module.module_description = request.POST.get("module_description")
            moduleEit_module_description = '{}'.format(request.POST.get("module_description"))
            module.module_photo = request.POST.get("module_photo")
            moduleEdit_module_photo = '{}'.format(request.POST.get("module_photo"))
            # insert_quesy_to_table = '''
            # update modules set module_name='{}', module_description='{}', module_photo='{}' where module_pk='{}'; '''\
            #     .format(moduleEdit_module_name, moduleEit_module_description, moduleEdit_module_photo, userEdit_pk)
            # cursor.execute(insert_quesy_to_table)
            # conn.commit()
            module.save()
            return render(request, 'index.html', {"it_user": user_is})
        else:
            return render(request, 'forms/forms_modules_edit.html',
                          {"pk": pk, "object": module, 'form': form, "it_user": user_is})
    except Modules.DoesNotExist:
        return render(request, 'index.html', {"it_user": user_is})


def lessonsEdit(request, name_parts, pk):
#    cursor = conn.cursor()
    user_is = request.user
    try:
        form = CreateLessonsForms
        module = Lessons.objects.get(id=pk)

        if request.method == "POST":
            userEdit_pk = '{}'.format(pk)
            module.id_modules_id = request.POST.get('id_modules')
            module_id_modules_id = '{}'.format(request.POST.get('id_modules'))
            module.lessons_name = request.POST.get("lessons_name")
            moduleEdit_lessons_name = '{}'.format(request.POST.get("lessons_name"))
            module.lessons_description = request.POST.get("lessons_description")
            moduleEdit_lessons_description = '{}'.format(request.POST.get("lessons_description"))
            module.is_parent = request.POST.get("is_parent")
            moduleEdit_is_parent = '{}'.format(request.POST.get("is_parent"))
            # insert_quesy_to_table = '''
            # update lessons set module_id='{}', lesson_name='{}', lesson_description='{}', is_parent='{}' where lesson_id='{}';'''\
            #     .format(module_id_modules_id, moduleEdit_lessons_name, moduleEdit_lessons_description,
            #                                            moduleEdit_is_parent,userEdit_pk )
            # cursor.execute(insert_quesy_to_table)
            # conn.commit()
            module.save()
            return render(request, 'index.html', {"it_user": user_is})
        else:
            return render(request, 'forms/forms_lessons_edit.html',
                          {"pk": pk, "object": module, 'form': form, "it_user": user_is})
    except Lessons.DoesNotExist:
        return render(request, 'index.html', {"it_user": user_is})


def lessonsmsgEdit(request, name_parts, pk):
#    cursor = conn.cursor()
    user_is = request.user
    try:
        form = CreateMessageLessonsForms
        module = LessonsMessage.objects.get(id=pk)

        if request.method == "POST":
            userEdit_pk = '{}'.format(pk)
            moduleEdit_id_lessons_id = '{}'.format(request.POST.get('id_lessons'))
            module.id_lessons_id = request.POST.get('id_lessons')
            type_value = request.POST.get('type_value')
            moduleEdit_type_value = '{}'.format(request.POST.get('type_value'))
            message_value = request.POST.get("message_value")
            message_photo = request.FILES.get("message_photos")
            message_caption = request.POST.get("message_caption")
            moduleEdit_message_caption = '{}'.format(request.POST.get("message_caption"))
            allMessages = AllMessage.objects.create(message_type=type_value, message_value=message_value,
                                                    message_caption=message_caption, message_photos=message_photo)
            module.id_AllMessages_id = allMessages.id
            if type_value == "text":
                moduleEdit_message_value = '{}'.format(request.POST.get("message_value"))
            else:
                moduleEdit_message_value = '{}'.format(request.FILES.get("message_photos"))
            # moduleEdit_id_AllMessages_id = '{}'.format(allMessages.id)
            # insert_quesy_to_table = '''
            # update all_messages set message_type='{}', message_caption='{}', message_value='{}' where message_id='{}';
            # '''.format(moduleEdit_type_value, moduleEdit_message_caption, moduleEdit_message_value, moduleEdit_id_AllMessages_id)
            # cursor.execute(insert_quesy_to_table)
            # conn.commit()
            # insert_quesy_to_table = '''
            # update lessons_messages set lesson_id='{}', message_id='{}' where id='{}';
            #  '''.format(moduleEdit_id_lessons_id, moduleEdit_id_AllMessages_id, userEdit_pk)
            # cursor.execute(insert_quesy_to_table)
            # conn.commit()
            module.save()
            return render(request, 'index.html', {"it_user": user_is})
        else:
            return render(request, 'forms/forms_lessonsmsg_edit.html',
                          {"pk": pk, "object": module, 'form': form, "it_user": user_is})
    except LessonsMessage.DoesNotExist:
        return render(request, 'index.html', {"it_user": user_is})


def questEdit(request, name_parts, pk):
#    cursor = conn.cursor()
    user_is = request.user
    try:
        form = CreateQuestForms
        module = Quest.objects.get(id=pk)

        if request.method == "POST":
            userEdit_pk = '{}'.format(pk)
            module.id_modules_id = request.POST.get('id_modules')
            moduleEdit_id_modules_id = '{}'.format(request.POST.get('id_modules'))
            module.id_lessons_id = request.POST.get("id_lessons")
            moduleEdit_id_lessons_id = '{}'.format(request.POST.get("id_lessons"))
            module.quest_name = request.POST.get("quest_name")
            moduleedit_quest_name = '{}'.format(request.POST.get("quest_name"))
            module.quest_description = request.POST.get("quest_description")
            moduleEdit_quest_description = '{}'.format(request.POST.get("quest_description"))
            # insert_quesy_to_table = '''
            # update quests set module_id='{}', lesson_id='{}', quest_name='{}', quest_description='{}' where quest_id='{}'; '''\
            #     .format(moduleEdit_id_modules_id, moduleEdit_id_lessons_id, moduleedit_quest_name,
            #                                            moduleEdit_quest_description, userEdit_pk)
            # cursor.execute(insert_quesy_to_table)
            # conn.commit()
            module.save()
            return render(request, 'index.html', {"it_user": user_is})
        else:
            return render(request, 'forms/forms_quest_edit.html',
                          {"pk": pk, "object": module, 'form': form, "it_user": user_is})
    except Quest.DoesNotExist:
        return render(request, 'index.html', {"it_user": user_is})


def questmsgEdit(request, name_parts, pk):
#    cursor = conn.cursor()
    user_is = request.user
    try:
        form = CreateMessageForQuestForms
        module = QuestMessage.objects.get(id=pk)

        if request.method == "POST":
            userEdit_pk = '{}'.format(pk)
            module.quest_id_id = request.POST.get('quest_id')
            moduleEdit_quest_id_id = '{}'.format(request.POST.get('quest_id'))
            type_value = request.POST.get('type_value')
            userEdit_type_value = '{}'.format(request.POST.get('type_value'))
            message_value = request.POST.get("message_value")
            messageEdit_value = '{}'.format(request.POST.get("message_value"))
            message_caption = request.POST.get("message_caption")
            message_photo = request.FILES.get("message_photos")
            messageEdit_caption = '{}'.format(request.POST.get("message_caption"))
            allMessages = AllMessage.objects.create(message_type=type_value, message_value=message_value,
                                                    message_caption=message_caption, message_photos=message_photo)
            module.id_AllMessages_id = allMessages.id
            if type_value == "text":
                moduleEdit_message_value = '{}'.format(request.POST.get("message_value"))
            else:
                moduleEdit_message_value = '{}'.format(request.FILES.get("message_photos"))
            moduleEdit_id_AllMessages_id = "{}".format(allMessages.id)
            # insert_quesy_to_table = '''
            #  update all_messages set message_type='{}', message_caption='{}', message_value='{}' where message_id='{}';
            #  '''.format(userEdit_type_value, messageEdit_value, messageEdit_caption, userEdit_pk)
            # cursor.execute(insert_quesy_to_table)
            # conn.commit()
            # insert_quesy_to_table = '''
            # update quests_messages set quest_id='{}', message_id='{}' where id='{}';
            # '''.format(moduleEdit_quest_id_id, moduleEdit_id_AllMessages_id)
            # cursor.execute(insert_quesy_to_table)
            # conn.commit()
            module.save()
            return render(request, 'index.html', {"it_user": user_is})
        else:
            return render(request, 'forms/forms_quest_msg_edit.html',
                          {"pk": pk, "object": module, 'form': form, "it_user": user_is})
    except QuestMessage.DoesNotExist:
        return render(request, 'index.html', {"it_user": user_is})


def choicequestEdit(request, name_parts, pk):
 #   cursor = conn.cursor()
    user_is = request.user
    try:
        form = CreateChoiceForQuestForms
        module = QuestChoices.objects.get(id=pk)

        if request.method == "POST":
            userEdit_pk = '{}'.format(pk)
            module.quest_id_id = request.POST.get('quest_id')
            moduleEdit_quest_id_id = '{}'.format(request.POST.get('quest_id'))
            module.choice_name = request.POST.get('choice_name')
            moduleEdit_choice_name = '{}'.format(request.POST.get('choice_name'))
            module.сhoice_description = request.POST.get('сhoice_description')
            moduleEdit_сhoice_description = '{}'.format(request.POST.get('сhoice_description'))
            module.is_True = request.POST.get("is_true")
            moduleEdit_is_True = '{}'.format(request.POST.get("is_true"))
            # insert_quesy_to_table = '''
            # update quests_choices set quest_id='{}', choice_name='{}', choice_description='{}', is_true='{}'
            # where choice_id='{}';'''.format(moduleEdit_quest_id_id, moduleEdit_choice_name,
            #                                            moduleEdit_сhoice_description, moduleEdit_is_True, userEdit_pk)
            # cursor.execute(insert_quesy_to_table)
            # conn.commit()
            module.save()
            return render(request, 'index.html', {"it_user": user_is})
        else:
            return render(request, 'forms/forms_quest_choice_edit.html',
                          {"pk": pk, "object": module, 'form': form, "it_user": user_is})
    except QuestChoices.DoesNotExist:
        return render(request, 'index.html', {"it_user": user_is})


def DoneCreate(request, name_parts):
    user_is = request.user
#    cursor = conn.cursor()

    if request.method == "POST":
        user = User()
        user.full_name = request.POST.get("full_name")
        user_full_name = '{}'.format(request.POST.get("full_name"))
        user.email = request.POST.get("email")
        user_email = '{}'.format(request.POST.get("email"))
        user.phone_number = request.POST.get("phone_number")
        user_phone_number = '{}'.format(request.POST.get("phone_number"))
        user.user_role = request.POST.get("user_role")
        user_user_role = '{}'.format(request.POST.get("user_role"))
        data_reg = '{}'.format(datetime.datetime.now())
        last_pk = User.objects.all().last().pk + 1
        # insert_quesy_to_table = '''
        # insert into user (data_reg, first_name, last_name, full_name, phone_number, email, is_confirm,
        #                  user_role, is_live, user_pk)
        # values ('{}', '', '', '{}', '{}', '{}', 0, '{}', 0, '{}');'''.format(data_reg, user_full_name, user_phone_number, user_email, user_user_role, last_pk)
        # cursor.execute(insert_quesy_to_table)
        # conn.commit()
        user.save()
    return render(request, 'index.html', {"it_user": user_is})


def ModuleCreate(request, name_parts):
    user_is = request.user
#    cursor = conn.cursor()
    if request.method == "POST":
        user = Modules()
        user.module_name = request.POST.get("module_name")
        user_module_name = '{}'.format(request.POST.get("module_name"))
        user.module_description = request.POST.get("module_description")
        user_description_module = '{}'.format(request.POST.get("module_description"))
        user.module_photo = request.FILES.get("module_photo")
        user_module_photo = '{}'.format(request.POST.get("module_photo"))
        #insert_quesy_to_table = '''
        # insert into modules (module_name, module_description, module_photo)
        # values ('{}', '{}', '{}');'''.format(user_module_name, user_description_module, user_module_photo)
        # cursor.execute(insert_quesy_to_table)
        # conn.commit()
        user.save()
    return render(request, 'index.html', {"it_user": user_is})


def LessonsCreated(request, name_parts):
    user_is = request.user
 #   cursor = conn.cursor()
    if request.method == "POST":
        user = Lessons()
        user.id_modules_id = request.POST.get('id_modules')
        user_id_modules_id = '{}'.format(request.POST.get('id_modules'))
        user.lessons_name = request.POST.get("lessons_name")
        user_lessons_name = '{}'.format(request.POST.get('lessons_name'))
        user.lessons_description = request.POST.get("lessons_description")
        user_lessons_description = '{}'.format(request.POST.get('lessons_description'))
        user.is_parent = request.POST.get("is_parent")
        user_is_parent = '{}'.format(request.POST.get('is_parent'))
        # insert_quesy_to_table = '''
        # insert into lessons (module_id, lesson_name, lesson_description, is_parent)
        # values ('{}', '{}', '{}', '{}');'''.format(user_id_modules_id, user_lessons_name, user_lessons_description,
        #                                            user_is_parent)
        # cursor.execute(insert_quesy_to_table)
        # conn.commit()
        user.save()
    return render(request, 'index.html', {"it_user": user_is})


def LessonsmsgCreated(request, name_parts):
 #   cursor = conn.cursor()
    user_is = request.user
    if request.method == "POST":
        user = LessonsMessage()
        user.id_lessons_id = request.POST.get('id_lessons')
        user_id_lessons_id = '{}'.format(request.POST.get('id_lessons'))
        type_value = request.POST.get('type_value')
        user_type_value = '{}'.format(request.POST.get('type_value'))
        message_value = request.POST.get("message_value")
        user_message_value = '{}'.format(request.POST.get('message_value'))
        message_photos = request.FILES.get("message_photos")
        message_caption = request.POST.get("message_caption")
        user_message_caption = '{}'.format(request.POST.get('message_caption'))
        allMessages = AllMessage.objects.create(message_type=type_value, message_photos=message_photos,
                                                message_value=message_value, message_caption=message_caption)
        user.id_AllMessages_id = allMessages.id
        if type_value == "text":
            moduleEdit_message_value = '{}'.format(request.POST.get("message_value"))
        else:
            moduleEdit_message_value = '{}'.format(request.FILES.get("message_photos"))
        user_id_AllMessages_id = '{}'.format(allMessages.id)
        # insert_quesy_to_table = '''
        # insert into all_messages(message_type, message_caption, message_value) values ('{}', '{}', '{}');
        # '''.format(user_type_value, user_message_value, user_message_caption)
        # cursor.execute(insert_quesy_to_table)
        # conn.commit()
        # insert_quesy_to_table = '''
        #  insert into lessons_messages(lesson_id, message_id)
        #  values ('{}', '{}');
        #  '''.format(user_id_lessons_id, user_id_AllMessages_id)
        # cursor.execute(insert_quesy_to_table)
        # conn.commit()
        user.save()
    return render(request, 'index.html', {"it_user": user_is})


def questCreated(request, name_parts):
#    cursor = conn.cursor()
    user_is = request.user
    if request.method == "POST":
        user = Quest()
        user.id_modules_id = request.POST.get('id_modules')
        user_id_modules_id = '{}'.format(request.POST.get('id_modules'))
        user.id_lessons_id = request.POST.get("id_lessons")
        user_id_lessons_id = '{}'.format(request.POST.get('id_lessons'))
        user.quest_name = request.POST.get("quest_name")
        user_quest_name = '{}'.format(request.POST.get('quest_name'))
        user.quest_description = request.POST.get("quest_description")
        user_quest_description = '{}'.format(request.POST.get('quest_description'))
        # insert_quesy_to_table = '''
        # insert into quests (module_id, lesson_id, quest_name, quest_description)
        # values ('{}', '{}', '{}', '{}');'''.format(user_id_modules_id, user_id_lessons_id, user_quest_name,
        #                                            user_quest_description)
        # cursor.execute(insert_quesy_to_table)
        # conn.commit()
        user.save()
    return render(request, 'index.html', {"it_user": user_is})


def questMsg(request, name_parts):
#    cursor = conn.cursor()
    user_is = request.user
    if request.method == "POST":
        user = QuestMessage()
        user.quest_id_id = request.POST.get('quest_id')
        user_quest_id_id = '{}'.format(request.POST.get('quest_id'))
        type_value = request.POST.get('type_value')
        user_type_value = '{}'.format(request.POST.get('type_value'))
        message_value = request.POST.get("message_value")
        user_message_value = '{}'.format(request.POST.get("message_value"))
        message_caption = request.POST.get("message_caption")
        message_photos = request.FILES.get("message_photos")
        user_message_photos = '{}'.format(request.FILES.get("message_photos"))
        user_message_caption = '{}'.format(request.POST.get("message_caption"))
        allMessages = AllMessage.objects.create(message_type=type_value, message_value=message_value,
                                                message_photos=message_photos,message_caption=message_caption)
        user.id_AllMessages_id = allMessages.id
        if type_value == "text":
            moduleEdit_message_value = '{}'.format(request.POST.get("message_value"))
        else:
            moduleEdit_message_value = '{}'.format(request.FILES.get("message_photos"))
        user_id_AllMessages_id = '{}'.format(allMessages.id)
        # insert_quesy_to_table = '''
        # insert into all_messages(message_type, message_caption, message_value) values ('{}', '{}', '{}');
        # '''.format(user_type_value, user_message_value, user_message_caption)
        # cursor.execute(insert_quesy_to_table)
        # conn.commit()
        # insert_quesy_to_table = '''
        #  insert into quests_messages(quest_id, message_id)
        #  values ('{}', '{}');
        #  '''.format(user_quest_id_id, user_id_AllMessages_id)
        # cursor.execute(insert_quesy_to_table)
        # conn.commit()
        user.save()
    return render(request, 'index.html', {"it_user": user_is})


def qestchoiceCreated(request, name_parts):
#    cursor = conn.cursor()
    user_is = request.user
    if request.method == "POST":
        user = QuestChoices()
        user.quest_id_id = request.POST.get('quest_id')
        user_quest_id_id = '{}'.format(request.POST.get('quest_id'))
        user.choice_name = request.POST.get('choice_name')
        user_choice_name = '{}'.format(request.POST.get('choice_name'))
        user.сhoice_description = request.POST.get('сhoice_description')
        user_сhoice_description = '{}'.format(request.POST.get('сhoice_description'))
        user.is_True = request.POST.get("is_true")
        user_is_True = '{}'.format(request.POST.get("is_true"))
        # insert_quesy_to_table = '''
        # insert into quests_choices (quest_id, choice_name, choice_description, is_true)
        # values ('{}', '{}', '{}', '{}');'''.format(user_quest_id_id, user_choice_name, user_сhoice_description,
        #                                            user_is_True)
        # cursor.execute(insert_quesy_to_table)
        # conn.commit()
        user.save()
    return render(request, 'index.html', {"it_user": user_is})


class LogOut(LogoutView):
    template_name = 'index.html'
    success_url = reverse_lazy('login')


def exportToExcel(request):
    users = User
    modules = Modules
    allmessages = AllMessage
    lessons = Lessons
    lessonsMessages = LessonsMessage
    quests = Quest
    questsMessage = QuestMessage
    questsChoices = QuestChoices
    list_models = [
        'users', 'modules', 'lessons', 'lessonsMessages', 'quests', 'questsMessage', 'questsChoices', 'allmessages', ]
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="users.xls"'
    wb = xlwt.Workbook(encoding='utf-8')
    for models in list_models:
        ws = wb.add_sheet(models)
        row_num = 0
        font_style = xlwt.XFStyle()
        font_style.font.bold = True
        if models == "users":
            columns = [
                'date_reg', 'first_name', 'last_name', 'full_name', 'phone_number', 'username', 'email', 'is_confirm',
                'user_role', 'is_live', 'subscribe', ]
            for col_num in range(len(columns)):
                ws.write(row_num, col_num, columns[col_num], font_style)
            font_style = xlwt.XFStyle()
            rows = users.objects.all().values_list('date_reg', 'first_name', 'last_name', 'full_name', 'phone_number',
                                                   'username', 'email', 'is_confirm', 'user_role', 'is_live',
                                                   'subscribe', )
            rows = [[x.strftime("%Y-%m-%d %H:%M") if isinstance(x, datetime.datetime) else x for x in row] for row in
                    rows]
            for row in rows:
                row_num += 1
                for col_num in range(len(row)):
                    ws.write(row_num, col_num, row[col_num], font_style)
        elif models == "modules":
            columns = [
                'module_name', 'module_description', 'module_photo', 'data_create_module', ]
            for col_num in range(len(columns)):
                ws.write(row_num, col_num, columns[col_num], font_style)
            font_style = xlwt.XFStyle()
            rows = modules.objects.all().values_list('module_name', 'module_description', 'module_photo',
                                                     'data_create_module', )

            rows = [[x.strftime("%Y-%m-%d %H:%M") if isinstance(x, datetime.datetime) else x for x in row] for row in
                    rows]
            for row in rows:
                row_num += 1
                for col_num in range(len(row)):
                    ws.write(row_num, col_num, row[col_num], font_style)
        elif models == "allmessages":
            columns = [
                'message_type', 'message_caption', 'message_value']
            for col_num in range(len(columns)):
                ws.write(row_num, col_num, columns[col_num], font_style)
            font_style = xlwt.XFStyle()
            rows = allmessages.objects.all().values_list('message_type', 'message_caption', 'message_value', )
            rows = [[x.strftime("%Y-%m-%d %H:%M") if isinstance(x, datetime.datetime) else x for x in row] for row in
                    rows]
            for row in rows:
                row_num += 1
                for col_num in range(len(row)):
                    ws.write(row_num, col_num, row[col_num], font_style)
        elif models == "lessons":
            columns = [
                'id_modules', 'lessons_name', 'lessons_description', 'is_parent', 'data_create_lessons']
            for col_num in range(len(columns)):
                ws.write(row_num, col_num, columns[col_num], font_style)
            font_style = xlwt.XFStyle()
            rows = lessons.objects.all().values_list('id_modules', 'lessons_name', 'lessons_description',
                                                   'data_create_lessons', )
            rows = [[x.strftime("%Y-%m-%d %H:%M") if isinstance(x, datetime.datetime) else x for x in row] for row in
                    rows]
            for row in rows:
                row_num += 1
                for col_num in range(len(row)):
                    ws.write(row_num, col_num, row[col_num], font_style)
        elif models == "lessonsMessages":
            columns = [
                'id_lessons', 'id_AllMessages']
            for col_num in range(len(columns)):
                ws.write(row_num, col_num, columns[col_num], font_style)
            font_style = xlwt.XFStyle()
            rows = lessonsMessages.objects.all().values_list('id_lessons', 'id_AllMessages', )
            rows = [[x.strftime("%Y-%m-%d %H:%M") if isinstance(x, datetime.datetime) else x for x in row] for row in
                    rows]
            for row in rows:
                row_num += 1
                for col_num in range(len(row)):
                    ws.write(row_num, col_num, row[col_num], font_style)
        elif models == "quests":
            columns = [
                'id_modules', 'id_lessons', 'quest_name', 'quest_description', 'data_create_quest',]
            for col_num in range(len(columns)):
                ws.write(row_num, col_num, columns[col_num], font_style)
            font_style = xlwt.XFStyle()
            rows = quests.objects.all().values_list('id_modules', 'id_lessons', 'quest_name', 'quest_description',
                                                    'data_create_quest', )
            rows = [[x.strftime("%Y-%m-%d %H:%M") if isinstance(x, datetime.datetime) else x for x in row] for row in
                    rows]
            for row in rows:
                row_num += 1
                for col_num in range(len(row)):
                    ws.write(row_num, col_num, row[col_num], font_style)
        elif models == "questsMessage":
            columns = [
                'quest_id', 'id_AllMessages', ]
            for col_num in range(len(columns)):
                ws.write(row_num, col_num, columns[col_num], font_style)
            font_style = xlwt.XFStyle()
            rows = questsMessage.objects.all().values_list('quest_id', 'id_AllMessages',)
            rows = [[x.strftime("%Y-%m-%d %H:%M") if isinstance(x, datetime.datetime) else x for x in row] for row in
                    rows]
            for row in rows:
                row_num += 1
                for col_num in range(len(row)):
                    ws.write(row_num, col_num, row[col_num], font_style)
        elif models == "questsChoices":
            columns = [
                'quest_id', 'choice_name', 'сhoice_description', 'is_True']
            for col_num in range(len(columns)):
                ws.write(row_num, col_num, columns[col_num], font_style)
            font_style = xlwt.XFStyle()
            rows = questsChoices.objects.all().values_list('quest_id', 'choice_name', 'сhoice_description', 'is_True',)
            rows = [[x.strftime("%Y-%m-%d %H:%M") if isinstance(x, datetime.datetime) else x for x in row] for row in
                    rows]
            for row in rows:
                row_num += 1
                for col_num in range(len(row)):
                    ws.write(row_num, col_num, row[col_num], font_style)
    wb.save(response)
    return response