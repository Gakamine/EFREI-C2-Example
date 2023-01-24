from django.contrib import admin
from django.utils.html import format_html

# Register your models here.
from .models import Computer,Data

@admin.register(Computer)
class ComputerAdmin(admin.ModelAdmin):
    def related_data(self, obj):
        return format_html("<a href='../data/?computer__id__exact={}'>See related data</a>",obj.id)
    list_display = ['hostname','ip_address','pub_date','related_data']
    search_fields = ['hostname','ip_address']
    list_filter = ('pub_date','hostname')

@admin.register(Data)
class DataAdmin(admin.ModelAdmin):
    def data(self, obj):
        if obj.is_file:
            return format_html("<a href='data:application/octet-stream;base64,{}' download>Download</a>",obj.data_content)
        else:
            return obj.data_content
    list_display = ['computer','data_type','pub_date','data','is_file']
    search_fields = ['computer__hostname']
    list_filter = ('pub_date','data_type','is_file')