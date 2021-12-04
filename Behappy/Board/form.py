from django import forms
from django.db import models
from django.db.models.base import Model
from django.forms import fields, widgets

from.models import Board, Member, studentBoard, graduateBoard, loveBoard

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['ID','password']
        widgets = {'password':forms.PasswordInput}


class signupForm(forms.ModelForm):
    password_check = forms.CharField(max_length=60, widget=forms.PasswordInput(attrs={'class':'pw2'}))
    class Meta:
        model = Member
        fields =  ['ID', 'password', 'password_check',]
        widgets = {
            'ID' : forms.TextInput(attrs={'class': 'ID'}),
            'password' : forms.PasswordInput(attrs={'class': 'pw1'}),
        }

class BoardWriteForm(forms.ModelForm):
    class Meta:
        model = Board
        fields = ['title', 'content', 'member']
        widgets ={
            'title' : forms.TextInput(attrs={'class' : 'title'}),
            'content' : forms.TextInput(attrs={'class':'content'}),
            'member' : forms.HiddenInput(),
        }

class studentBoardWriteForm(forms.ModelForm):
    class Meta:
        model = studentBoard
        fields = ['title', 'content', 'member']
        widgets ={
            'title' : forms.TextInput(attrs={'class' : 'title'}),
            'content' : forms.TextInput(attrs={'class':'content'}),
            'member' : forms.HiddenInput(),
        }


class graduateBoardWriteForm(forms.ModelForm):
    class Meta:
        model = graduateBoard
        fields = ['title', 'content', 'member']
        widgets ={
            'title' : forms.TextInput(attrs={'class' : 'title'}),
            'content' : forms.TextInput(attrs={'class':'content'}),
            'member' : forms.HiddenInput(),
        }

class loveBoardWriteForm(forms.ModelForm):
    class Meta:
        model = loveBoard
        fields = ['title', 'content', 'member']
        widgets ={
            'title' : forms.TextInput(attrs={'class' : 'title'}),
            'content' : forms.TextInput(attrs={'class':'content'}),
            'member' : forms.HiddenInput(),
        }