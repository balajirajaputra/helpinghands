from django.contrib import admin
from hhands.models import Useraccount, Customers, CustomerLogin, DrugUtilization, DrugReimbursements, DRReimTotals
from hhands.models import HcpInformation, HcpLocation, HcpUtilization, MedicareDrugs
from hhands.models import DHUtilization, DrugsHeader, DRreimbursements

# Register your models here.
admin.site.register(Useraccount)
admin.site.register(Customers)
admin.site.register(CustomerLogin)
#admin.site.register(DrugUtilization)
#admin.site.register(DrugReimbursements)
#admin.site.register(MedicareDrugs)
admin.site.register(HcpInformation)
admin.site.register(HcpLocation)
admin.site.register(HcpUtilization)

admin.site.register(DHUtilization)
admin.site.register(DrugsHeader)
admin.site.register(DRreimbursements)

admin.site.register(DRReimTotals)
