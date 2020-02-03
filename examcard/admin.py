from django.contrib import admin
from examcard.models import StudentProfile, StudentUnit,Unit,Fee, Log,Report

# Register your models here.
@admin.register(StudentProfile)
class StudentProfileAdmin(admin.ModelAdmin):
    list_display = ["first_name","sirname", "last_name","adm_number"]
    link_display = ["adm_number"]
    
    
@admin.register(StudentUnit)
class StudentUnitAdmin(admin.ModelAdmin):
    list_display = ["profile", "student_unit"]
    link_display =["student_unit"]

@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
    list_display = ["unit_name","unit_code"]
    link_display = ["unit_code"]
    
@admin.register(Fee)
class FeeAdmin(admin.ModelAdmin):
    list_display = ["profile","is_completed"]
    link_display = ["profile"]

@admin.register(Log)
class LogAdmin(admin.ModelAdmin):
    list_display = ["user", "profile", "fee","timstamp"]
    link_display = ["profile"]
    
@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ["user", "student", "message"]

    
