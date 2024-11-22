from django.shortcuts import render
from testapp.models import Device

# Create your views here.
def index(request):
    devices = Device.objects.all()
    return render(request, 'testapp/index.html', context={"devices": devices})