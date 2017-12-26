# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render

from django.http import HttpResponse
from django.template.loader import get_template


from .models import Work
from django import forms


from django.http import HttpResponseRedirect
from django.urls import reverse

from .forms import UserInfo
from openpyxl import Workbook
from openpyxl import  load_workbook
# Create your views here.

i=0
j=0
def user_list(request):
	global i
	f_obj = UserInfo()
	if request.method ==  'POST':
		#wb = Workbook()
		wb = load_workbook('roll number.xlsx')
		ws = wb.active
		ws.title = "兼职报名统计"
		number = ws.cell(row=2,column=1)
		number.value = "序号"
		#name = ws.cell('A2')
		name = ws.cell(row=2,column=2)
		name.value = "名字"
		#phone = ws.cell('B2')
		phone = ws.cell(row=2,column=3)
		phone.value = "手机号"
		sex = ws.cell(row=2, column=4)
		#sex = ws.cell('C2')
		sex.value = "性别"
		#school = ws.cell('D2')
		school = ws.cell(row=2, column=5)
		school.value = "学校"


		user_input_obj = UserInfo(request.POST)
		if user_input_obj.is_valid():
			i +=1
			data = user_input_obj.clean()
			f_name = user_input_obj.cleaned_data['name']
			f_phone = user_input_obj.cleaned_data['phone']
			f_sex = user_input_obj.cleaned_data['sex']
			f_school = user_input_obj.cleaned_data['school']
			ws.append({'A':i,'B':f_name,'C':f_phone,'D':f_sex,'E':f_school})
			wb.save('roll number.xlsx')
			print f_name
		else:
			error_msg = user_input_obj.errors
			return render(request,'user_list.html',{'obj':user_input_obj,'errors':error_msg})
	return render(request,'user_list.html',context={'obj':f_obj})



def index(request):
	template = get_template('index.html')
	html = template.render(locals())
	return HttpResponse(html)

def login(request):
	global i
	#f_obj = UserInfo()
	print'enter login process'
	try:
		f_name = request.GET['username']
		print f_name
	except:
		f_name = 'default'
		print 'no data'
	'''if request.method == 'POST':

		user_input_obj = UserInfo(request.POST)
		f_name = request.GET['name']
		print 'is too'
		if user_input_obj.is_valid():
			print f_sex
		else:
			return render(request, 'login.html', {'obj': user_input_obj})'''
	return render(request,'login.html')

def contact(request):
	template = get_template('contact.html')
	html = template.render(locals())
	return HttpResponse(html)

def xls_process(UserInfo):
	global j
	j +=1
	user_input_obj = UserInfo
	wb = load_workbook('roll number.xlsx')
	ws = wb.active
	ws.title = "兼职报名统计"
	number = ws.cell(row=2, column=1)
	number.value = "序号"
	# name = ws.cell('A2')
	name = ws.cell(row=2, column=2)
	name.value = "名字"
	# phone = ws.cell('B2')
	phone = ws.cell(row=2, column=3)
	phone.value = "手机号"
	sex = ws.cell(row=2, column=4)
	# sex = ws.cell('C2')
	sex.value = "性别"
	# school = ws.cell('D2')
	school = ws.cell(row=2, column=5)
	school.value = "学校"
	roll_content = ws.cell(row=2, column=6)
	roll_content.value = "报名信息"
	f_name = user_input_obj.cleaned_data['name']
	f_phone = user_input_obj.cleaned_data['phone']
	f_sex = user_input_obj.cleaned_data['sex']
	f_school = user_input_obj.cleaned_data['school']
	f_roll = user_input_obj.cleaned_data['content']
	ws.append({'A': j, 'B': f_name, 'C': f_phone, 'D': f_sex, 'E': f_school,'F':f_roll})
	wb.save('roll number.xlsx')

def notic(request):

	#words = 'World!'
	works = Work.objects.all()
	f_obj = UserInfo()
	if request.method ==  'POST':
		user_obj = UserInfo(request.POST)
		if user_obj.is_valid():
			data = user_obj.clean()
			xls_process(user_obj)
			print data
		else:
			erro_msg = user_obj.errors
			return render(request,'user_list.html',{'obj':user_obj,'errors':erro_msg})
	#return render(request,'user_list.html',context={'obj':f_obj})
	return render(request, 'notic.html', context={'notices': works,'obj':f_obj})
#def student(request):
#	students = Student.objects.all()
#	return render(request,'student.html',context={'students':students})

#def student(request):
#    students = Student.objects.all()
#    if request.method == 'POST':
#        form = StudentForm(request.POST)
#        if form.is_valid():
#            cleaned_data = form.cleaned_data
#            student = Student()
#            student.name = cleaned_data['name']
#            student.sex = cleaned_data['sex']
#            student.email = cleaned_data['email']
#            student.profession = cleaned_data['profession']
#            student.qq = cleaned_data['qq']
#            student.phone = cleaned_data['phone']
#            student.save()
#            return HttpResponseRedirect(reverse('student'))
#    else:
##        form = StudentForm()
#
#    context = {
#        'students': students,
#        'form': form,
#    }
#    return render(request, 'student.html', context=context)
