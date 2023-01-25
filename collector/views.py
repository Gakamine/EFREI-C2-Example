from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from .models import Computer,Data
import hashlib

# Create your views here.
def index(request=None, hostname=None, ip=None,data_type=None,data_content=None,data_hash=None):
    if hostname and ip and data_type and data_content:
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
