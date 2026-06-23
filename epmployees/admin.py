from django.contrib import admin
from .models import Employee

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'department', 'salary')
    search_fields = ('name', 'email', 'department')
    list_filter = ('department',)

admin.site.register(Employee, EmployeeAdmin)