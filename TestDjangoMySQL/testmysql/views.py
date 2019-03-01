from django.shortcuts import render
from django.http import HttpResponse

#load data from DB into views
from testmysql.models import Useraccount

# Create your views here.
def Home(request):
    #return render(request,'testmysql/Home.html')
    data_list = Useraccount.objects.order_by('ua_l_name')
    data_dict = {'ua_l_name':data_list}
    return render(request,'testmysql/Home.html',context=data_dict)

def Visuals(request):
    return render(request,'testmysql/Visuals.html')
