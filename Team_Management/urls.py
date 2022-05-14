from . import views
from django.urls import path
from Team_Management.views import TaskJson
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView

urlpatterns = [
    path('', views.toHome, name="Home"),
    path('Tasks_Json/', TaskJson.as_view(), name="TasksJsonView"),
    path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('img\Logo.png'))),
    path('signup', views.signup, name="signup"),
    path('login', views.log_in, name="login"),
    path('signout', views.signout, name="signout"),
    path('activate/<uidb64>/<token>', views.activate, name="activate"),
    path('createTeam', views.create_team, name="createTeam"),
    path('toCreateTeam', views.toCreateTeam, name="toCreateTeam"),
    path('toViewTeam', views.toViewTeam, name="toViewTeam"),
    path('toTeam', views.toTeam, name="toTeam"),
    path('toAddMembers', views.toAddMembers, name="toAddMembers"),
    path('addMembers', views.addMembers, name="addMembers"),
    path('addTask', views.addTask, name="addTask"),
    path('taskDetails/<tid>', views.taskDetails, name="taskDetails"),
    path('taskDelete/<tid>', views.taskDelete, name="taskDelete"),
    path('memberRemove/<tm>/<mem>', views.memberRemove, name="memberRemove"),
    path('teamRemove/<tm>', views.teamRemove, name="teamRemove"),
    path('leaveTeam/<tm>/<mem>', views.leaveTeam, name="leaveTeam"),
    path('JoinTeam/<tm>/<mem>/<id>', views.JoinTeam, name="JoinTeam"),
    path('RequestReject/<id>', views.RequestReject, name="RequestReject"),
    path('toViewTeam_Req', views.toViewTeam_Req, name="toViewTeam_Req"),


]
