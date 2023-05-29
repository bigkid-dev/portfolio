from django.contrib import admin
from .models import Customer
# Register your models here.
# class CustomerAdmin(admin.ModelAdmin):

#     list_display = ('sex', 'gender', 'created_by', 'created', 'status')
#     readonly_fields = ('created',)

#     def __str__(self, obj):
#         return obj.name + " " + obj.last_name
    

admin.site.register(Customer)