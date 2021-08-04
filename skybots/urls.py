from django.urls import path
from .views import *
from skybots import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', LoginUser.as_view(), name="login"),
    path('logout/', LogOut.as_view(), name="logout"),
    path('export_toexcel/', views.exportToExcel, name="export_to_excel"),
    path('<str:name_parts>/', PartsView.as_view(), name="parts"),
    path('<str:name_parts>/<int:pk>/edit/', EditModels.as_view(), name="userEdit"),
    path('<str:name_parts>/<int:pk>/edituser/', views.userEdit, name="userEdits"),
    path('<str:name_parts>/<int:pk>/editthemes/', views.themesEdit, name="themesEdits"),
    path('<str:name_parts>/<int:pk>/editmodule/', views.moduleEdit, name="moduleEdit"),
    path('<str:name_parts>/<int:pk>/editlessons/', views.lessonsEdit, name="lessonsEdit"),
    path('<str:name_parts>/<int:pk>/editlessonsmsg/', views.lessonsmsgEdit, name="lessonsmsgEdit"),
    path('<str:name_parts>/<int:pk>/editquest/', views.questEdit, name="questEdit"),
    path('<str:name_parts>/<int:pk>/editquestmsg/', views.questmsgEdit, name="questmsgEdit"),
    path('<str:name_parts>/<int:pk>/editchoicequest/', views.choicequestEdit, name="choicequestEdit"),
    path('<str:name_parts>/<int:pk>/deleteuser/', views.userDelete, name="deleteUser"),
    path('<str:name_parts>/<int:pk>/deletethemes/', views.themesDelete, name="deleteThemes"),
    path('<str:name_parts>/<int:pk>/deletemodule/', views.moduleDelete, name="moduleDelete"),
    path('<str:name_parts>/<int:pk>/deletelessons/', views.lessonsDelete, name="lessonsDelete"),
    path('<str:name_parts>/<int:pk>/deletelessonsmsg/', views.lessonsmsgDelete, name="lessonsmsgDelete"),
    path('<str:name_parts>/<int:pk>/deletelesquest/', views.questsDelete, name="questsDelete"),
    path('<str:name_parts>/<int:pk>/deletelesquestmsg/', views.questsmsgDelete, name="questsmsgDelete"),
    path('<str:name_parts>/<int:pk>/deletelesquestchoice/', views.questschoiceDelete, name="questschoiceDelete"),
    path('<str:name_parts>/add/', CreateModels.as_view(), name="parts_add"),
    path('<str:name_parts>/add/done', views.DoneCreate, name="donecreate"),
    path('<str:name_parts>/add/donethemes', views.ThemesCreate, name="themesCreate"),
    path('<str:name_parts>/add/doneIS', views.ModuleCreate, name="moduleCreate"),
    path('<str:name_parts>/add/doneLes', views.LessonsCreated, name="lessonsCreated"),
    path('<str:name_parts>/add/doneLesMSg', views.LessonsmsgCreated, name="lessonsmsgCreated"),
    path('<str:name_parts>/add/donequest', views.questCreated, name="questCreated"),
    path('<str:name_parts>/add/donequestmsg', views.questMsg, name="questmsgCreated"),
    path('<str:name_parts>/add/donequestchoice', views.qestchoiceCreated, name="questChoiceCreated"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)