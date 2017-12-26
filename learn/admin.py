
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin

#from .models import Student
from .models import Work 
# Register your models here.

class WorkAdmin(admin.ModelAdmin):
	list_display = ('name','work_time','work_location')
#	list_filter = ('sex','status','created_time')
#	search_fields = ('name','profession')
	fieldsets = (
		(None,{
		'fields':(
				'name',
				('work_time','work_location'),
#				('work_content','work_requirement','payment'),
#:				'roll_number',
				)
		}
		
		),
	) 

admin.site.register(Work,WorkAdmin)
#admin.site.register(Student,StudentAdmin)
