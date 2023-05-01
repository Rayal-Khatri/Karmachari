from django.contrib import admin
from .models import *
from .forms import *
from django.urls import reverse
from django.utils.html import format_html
from django.urls import path
from django.db.models import Q
from django.db.models import Count
import json
from .charts import attendance_chart_data
from django.db.models.functions import TruncDate
import matplotlib.pyplot as plt
import numpy as np
import io
import base64

# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    list_display=('user','department','phone_number','dob','post')
    # fields=('user','department','phone_number','dob','profileimg')
    readonly_fields = ['img_preview']
    
    
    
class ScheduleAdmin(admin.ModelAdmin):
    list_display=('department','schedule_start','schedule_end')
    
    
    
class LeavesAdmin(admin.ModelAdmin):
    list_display=('user','subject','date','leave_type','less_message','status')
    def less_message(self,obj):
        return obj.message[:50]
    
    

class NoticeAdmin(admin.ModelAdmin):
    list_display=('title','created_at','department','less_context')
    
    def less_context(self,obj):
        return obj.context[:50]
    
class DateFilter(admin.DateFieldListFilter):
    title = 'Date'
    

class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('name', 'dateOfQuestion', 'checkInTime', 'checkOutTime', 'status')
    search_fields = ['name', 'user__username']
    list_filter = [('dateOfQuestion', admin.DateFieldListFilter)]
    

        
class PayrollAdmin(admin.ModelAdmin):
    # form = PayrollForm
    fields = ('user','basic_pay', 'deductions')
    readonly_fields = ['net_pay']
    list_filter = [
        ('date', DateFilter),
    ]
    
    
class SalaryAdmin(admin.ModelAdmin):
    list_display=('post','hourly_rate')
    
admin.site.register(Profile,ProfileAdmin)
admin.site.register(Notice,NoticeAdmin)
admin.site.register(Department)
admin.site.register(Leaves,LeavesAdmin)
admin.site.register(Events)
admin.site.register(Payroll,PayrollAdmin)
admin.site.register(AllowedIP)
admin.site.register(Salary,SalaryAdmin)
admin.site.register(Schedule,ScheduleAdmin)
admin.site.register(Attendance,AttendanceAdmin)


