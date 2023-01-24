from django.db import models

# Create your models here.
class Computer(models.Model):
    hostname = models.CharField(max_length=200)
    ip_address = models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.hostname

class Data(models.Model):
    computer = models.ForeignKey(Computer, on_delete=models.CASCADE)
    data_type = models.CharField(max_length=200)
    data_content = models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_now_add=True)
    is_file = models.BooleanField(default=False)
    def __str__(self):
        return self.computer.hostname