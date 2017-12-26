# coding:utf-8
from __future__ import unicode_literals

from django import forms

#from .models import Work

class UserInfo(forms.Form):
	SEX_LIST =(
		('男','男'),
		('女','女'),
	)
	SCHOOL_LIST =(
		('海南大学','海南大学'),
		( '海南医学院', '海南医学院'),
		('海南外国语职业学院', '海南外国语职业学院'),
		('海南经济贸易学院', '海南经济贸易学院'),
	)
	name = forms.CharField()
	#sex  = forms.CharField()
	#sex = forms.IntegerField(
	sex = forms.CharField(
		widget =  forms.Select(choices=SEX_LIST)
	)
	phone = forms.CharField()
	#school = forms.CharField()
	#school = forms.IntegerField(
	school = forms.CharField(
		widget =  forms.Select(choices=SCHOOL_LIST)
	)
	content = forms.CharField()


