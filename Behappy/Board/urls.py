from django import urls
from django.conf.urls import url
from django.urls import path

from FindLocation.views import showDiffer
from . import views

urlpatterns = [
    
    #새내기 게시판
    path('nonMemberMain/', views.nonMemberMain, name='nonMemberMain'),
    path('nonMemberDetail/<int:boardid>/', views.nonMemberDetail, name='nonMemberDetail'),
    path('main/', views.main, name='main'),
    path('write/', views.write, name='write'),
    path('detail/<int:boardid>/', views.detail, name='detail'),
    path('delete/<int:boardid>', views.delete, name='delete'),
    path('update/<int:boardid>/', views.update, name='update'),
    url('post/(?P<id>[0-9]+)$', views.detail, name='detail'),

    path('login/', views.login, name='login'),
    path('signUp/', views.signUp, name='signUp'),
    path('logout/', views.logout, name='logout'),


    #재학생 게시판
    path('studentnonMemberMain/', views.studentnonMemberMain, name='studentnonMemberMain'),
    path('studentnonMemberDetail/<int:boardid>/', views.studentnonMemberDetail, name='studentnonMemberDetail'),
    path('studentmain/', views.studentmain, name='studentmain'),
    path('studentwrite/', views.studentwrite, name='studentwrite'),
    path('studentdetail/<int:boardid>/', views.studentdetail, name='studentdetail'),
    path('studentdelete/<int:boardid>', views.studentdelete, name='studentdelete'),
    path('studentupdate/<int:boardid>/', views.studentupdate, name='studentupdate'),
    url('post/(?P<id>[0-9]+)$', views.detail, name='detail'),

    path('studentlogin/', views.studentlogin, name='studentlogin'),
    path('studentsignUp/', views.studentsignUp, name='studentsignUp'),
    path('studentlogout/', views.studentlogout, name='studentlogout'),




] 