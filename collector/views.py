from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from .models import Computer,Data

# Create your views here.
def index(request=None, hostname=None, ip=None,data_type=None,data=None,file_type=False):
    if hostname and ip and data_type and data:
        host=Computer.objects.filter(hostname=hostname,ip_address=ip)
        if host.exists():
            host=host[0]
        else:
            host=Computer.objects.create(hostname=hostname,ip_address=ip)
            host.save()
        data=Data.objects.create(computer=host,data_type=data_type,data_content=data,is_file=file_type)
        data.save()
    return render(request, 'index.html')