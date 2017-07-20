# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import *
# Register your models here.
class companymodeladmin(admin.ModelAdmin):
	list_display = ["Name","CreateDate","ModifiedDate"]
	class Meta:
		model=Company
admin.site.register(Company,companymodeladmin)

class Departmentmodeladmin(admin.ModelAdmin):
	list_display = ["DepartmentName","CreateDate","ModifiedDate"]
	class Meta:
		model=Department
admin.site.register(Department,Departmentmodeladmin)

class Functionsmodeladmin(admin.ModelAdmin):
	list_display = ["FunctionName","CreateDate","ModifiedDate"]
	class Meta:
		model=Functions_Master

admin.site.register(Functions_Master,Functionsmodeladmin)

class Employeemodeladmin(admin.ModelAdmin):
	list_display = ["Title","CreateDate","ModifiedDate"]
	class Meta:
		model=Employee

admin.site.register(Employee,Employeemodeladmin)

class CourtSeatmodeladmin(admin.ModelAdmin):
	list_display = ["CourtSeat","CreateDate","ModifiedDate"]
	class Meta:
		model=CourtSeat_Master

admin.site.register(CourtSeat_Master,CourtSeatmodeladmin)

class CourtTypemodeladmin(admin.ModelAdmin):
	list_display = ["CourtType","CreateDate","ModifiedDate"]
	class Meta:
		model=CourtType_Master

admin.site.register(CourtType_Master,CourtTypemodeladmin)

class WorkBench1modeladmin(admin.ModelAdmin):
	list_display = ["WorkBench","CreateDate","ModifiedDate"]
	class Meta:
		model=WorkBench1_Master

admin.site.register(WorkBench1_Master,WorkBench1modeladmin)

class WorkBench2modeladmin(admin.ModelAdmin):
	list_display = ["WorkBench","CreateDate","ModifiedDate"]
	class Meta:
		model=WorkBench2_Master

admin.site.register(WorkBench2_Master,WorkBench2modeladmin)

class WorkBench3modeladmin(admin.ModelAdmin):
	list_display = ["WorkBench","CreateDate","ModifiedDate"]
	class Meta:
		model=WorkBench3_Master

admin.site.register(WorkBench3_Master,WorkBench3modeladmin)

class WorkBench4modeladmin(admin.ModelAdmin):
	list_display = ["WorkBench","CreateDate","ModifiedDate"]
	class Meta:
		model=WorkBench4_Master

admin.site.register(WorkBench4_Master,WorkBench4modeladmin)

class WorkFlowStatusmodeladmin(admin.ModelAdmin):
	list_display = ["WorkFlowStatus","CreateDate","ModifiedDate"]
	class Meta:
		model=WorkFlowStatus_Master

admin.site.register(WorkFlowStatus_Master,WorkFlowStatusmodeladmin)

class SiteStatusmodeladmin(admin.ModelAdmin):
	list_display = ["Status","CreateDate","ModifiedDate"]
	class Meta:
		model=SiteStatus_Master

admin.site.register(SiteStatus_Master,SiteStatusmodeladmin)

class PositionWeightmodeladmin(admin.ModelAdmin):
	list_display = ["Percentage","CreateDate","ModifiedDate"]
	class Meta:
		model=PositionWeight_Master

admin.site.register(PositionWeight_Master,PositionWeightmodeladmin)

class Gendermodeladmin(admin.ModelAdmin):
	list_display = ["Gender","CreateDate","ModifiedDate"]
	class Meta:
		model=Gender_Master

admin.site.register(Gender_Master,Gendermodeladmin)

class Countrymodeladmin(admin.ModelAdmin):
	list_display = ["Country","CreateDate","ModifiedDate"]
	class Meta:
		model=Country_Master

admin.site.register(Country_Master,Countrymodeladmin)

class Tablemodeladmin(admin.ModelAdmin):
	list_display = ["Table_Name","ModifiedDate"]
	class Meta:
		model=TABLE_AUDIT

admin.site.register(TABLE_AUDIT,Tablemodeladmin)
