from django.shortcuts import render
from django.http import HttpResponse

from testmysql2.models import HcpInformation
# Create your views here.
def index(request):
    #hcp_data = HcpInformation.objects.values_list('hcp_id').order_by('hcp_id')
    hcp_data = HcpInformation.objects.order_by('hcp_id')
    HCP_Dict = {'hcp_id':hcp_data}
    return render(request,'testmysql2/index.html',context=HCP_Dict)

# ref - https://docs.djangoproject.com/en/2.1/ref/models/querysets/#django.db.models.query.QuerySet.values
