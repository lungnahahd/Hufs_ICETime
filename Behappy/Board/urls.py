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
    


    #졸업생 게시판
    path('graduatenonMemberMain/', views.graduatenonMemberMain, name='graduatenonMemberMain'),
    path('graduatenonMemberDetail/<int:boardid>/', views.graduatenonMemberDetail, name='graduatenonMemberDetail'),
    path('graduatemain/', views.graduatemain, name='graduatemain'),
    path('graduatewrite/', views.graduatewrite, name='graduatewrite'),
    path('graduatedetail/<int:boardid>/', views.graduatedetail, name='graduatedetail'),
    path('graduatedelete/<int:boardid>', views.graduatedelete, name='graduatedelete'),
    path('graduateupdate/<int:boardid>/', views.graduateupdate, name='graduateupdate'),
    url('post/(?P<id>[0-9]+)$', views.detail, name='detail'),

    path('graduatelogin/', views.graduatelogin, name='graduatelogin'),
    path('graduatesignUp/', views.graduatesignUp, name='graduatesignUp'),
    path('graduatelogout/', views.graduatelogout, name='graduatelogout'),



    #연애상담 게시판
    path('lovenonMemberMain/', views.lovenonMemberMain, name='lovenonMemberMain'),
    path('lovenonMemberDetail/<int:boardid>/', views.lovenonMemberDetail, name='lovenonMemberDetail'),
    path('lovemain/', views.lovemain, name='lovemain'),
    path('lovewrite/', views.lovewrite, name='lovewrite'),
    path('lovedetail/<int:boardid>/', views.lovedetail, name='lovedetail'),
    path('lovedelete/<int:boardid>', views.lovedelete, name='lovedelete'),
    path('loveupdate/<int:boardid>/', views.loveupdate, name='loveupdate'),
    url('post/(?P<id>[0-9]+)$', views.detail, name='detail'),

    path('lovelogin/', views.lovelogin, name='lovelogin'),
    path('lovesignUp/', views.lovesignUp, name='lovesignUp'),
    path('lovelogout/', views.lovelogout, name='lovelogout'),






] 