
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
#class Student(models.Model):
#	name = models.CharField(max_length = 128,verbose_name = "name")
#	work_time = models.CharField(max_length = 128,verbose_name = "work time")
#	work_location= models.CharField(max_length = 128,verbose_name = "work location")
##	work_content= models.CharField(max_length = 128,verbose_name = "work content")
##	work_requirment= models.CharField(max_length = 128,verbose_name = "work requirment")
##	payment= models.CharField(max_length = 128,verbose_name = "payment")
##	roll_number= models.CharField(max_length = 128,verbose_name = "roll number")
##	remarks = models.CharField(max_length = 128,verbose_name = "remarks")
##	work_time= models.DateTimeField(auto_now_add = True,editable = False, verbose_name = "work time")
#
#	def __unicode__(self):
#		return '<Student: {}>'.format(self.name)
#
#	class Meta:
#		verbose_name = verbose_name_plural = "information of students"
#
class Work(models.Model):

	name = models.CharField(max_length = 128,verbose_name = "名字")
	work_time = models.CharField(max_length = 128,verbose_name = "工作时间")
	work_location= models.CharField(max_length = 128,verbose_name = "工作地点")
	#slug = models.CharField(max_length = 128,verbose_name = "slug")
#	work_content= models.CharField(max_length = 128,verbose_name = "work content")
#	work_requirment= models.CharField(max_length = 128,verbose_name = "work requirment")
#	payment= models.CharField(max_length = 128,verbose_name = "payment")
#	roll_number= models.CharField(max_length = 128,verbose_name = "roll number")
#	remarks = models.CharField(max_length = 128,verbose_name = "remarks")
#	work_time= models.DateTimeField(auto_now_add = True,editable = False, verbose_name = "work time")

	def __unicode__(self):
		#return '<Work: {}>'.format(self.name)
		return self.name

	class Meta:
		verbose_name = verbose_name_plural = "兼职公告"
