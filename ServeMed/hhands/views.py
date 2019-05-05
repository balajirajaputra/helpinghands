from django.shortcuts import render
from django.contrib.auth import login, logout
from django.http import HttpResponse
from hhands.models import Customers, CustomerLogin, HcpInformation, DHUtilization, DrugsHeader, DRreimbursements, DRReimTotals
from hhands.forms import NewCustomerForm, NewCustomerLogin
from django.core.urlresolvers import reverse_lazy
#from django.urls import reverse
from django.views.generic import (View,TemplateView,
                                ListView,DetailView,
                                CreateView,DeleteView,
                                UpdateView)
from . import forms
from . import models

import json
import csv
from django.http import JsonResponse

from matplotlib import pylab
from pylab import *
from io import BytesIO
import PIL, PIL.Image

from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework.response import Response

#below for braintree
# import braintree
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.utils.decorators import method_decorator
from django.views import generic

from django.conf import settings

from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.db.models import Count

from collections import defaultdict

User = get_user_model()

# Create your views here.
class ChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        qs_count = User.objects.all().count()
        labels =  ['Users', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange']
        default_items = [qs_count, 12, 22, 33, 26, 31]
        data = {
                "labels": labels,
                "default": default_items,
            }
        return Response(data)

class BarChart(APIView):
    authentication_classes = []
    permission_classes = []


    def get(self, request, format=None):
        data = []
        labels = []
        label1 = models.DRReimTotals.objects.all().values('service_state').order_by('service_state')
        data1 = models.DRReimTotals.objects.all().values('total_amt_reimbursed').order_by('service_state')
        for c in data1:
            data.append(c['total_amt_reimbursed'])
        for c in label1:
            labels.append(c['service_state'])
        # data = [3945729,	3081283,	1259027,	7794121,	17199065,	1460087,	3107792,	240538,	533138,	24410986,	2785024,	2604548,	745899,	814449,	6655007,	3160828,	655556,	1362546,	1585895,	4901896,	7627929,	394118,	11807520,	4249950,	6547362,	1254299,	1480934,	4198707,	206544,	149317,	768321,	7993158,	3076202,	2033173,	6701550,	10876055,	1691786,	4194356,	24669208,	3081526,	1401776,	293651,	10216508, 24373081, 982388,	3689422,	887886,	8198730,	922286,	2213878,	227553]
        # labels =  ['AK',	'AL',	'AR',	'AZ',	'CA',	'CO',	'CT',	'DC',	'DE',	'FL',	'GA',	'HI',	'IA',	'ID',	'IL',	'IN',	'KS',	'KY',	'LA',	'MA',	'MD',	'ME',	'MI',	'MN',	'MO',	'MS',	'MT',	'NC',	'ND',	'NE',	'NH',	'NJ',	'NM',	'NV',	'NY',	'OH',	'OK',	'OR',	'PA',	'RI',	'SC',	'SD',	'TN',	'TX',	'UT',	'VA',	'VT',	'WA',	'WI',	'WV',	'WY']
        default_items = data
        data = {
                "labels": labels,
                "default": default_items,
            }
        return Response(data)

def getimage(request):
    # construct the graph
    x = arange(0, 2*pi, 0.01)
    s = cos(x)**2
    plot(x,s)

    xlabel('xlabel(x)')
    ylabel('ylabel(y)')
    title('Simple Graph!')
    grid(True)

    # Store Image in a string buffer
    buffer = BytesIO()
    canvas = pylab.get_current_fig_manager().canvas
    canvas.draw()
    pilImage = PIL.Image.frombytes("RGB", canvas.get_width_height(), canvas.tostring_rgb())
    pilImage.save(buffer, "PNG")
    pylab.close()

    # Send buffer in a http response the the browser with the mime type image/png set
    return HttpResponse(buffer.getvalue(), content_type="image/png")


class testpage(TemplateView):
    template_name = 'hhands/test.html'


class thankspage(TemplateView):
    template_name = 'hhands/thanks.html'

class signup(CreateView):
    form_class = forms.UserSignUpForm
    success_url = reverse_lazy('login')
    template_name = 'hhands/signup.html'

def home(request):
    return render(request,'hhands/home.html')

def checkout(request):
    return render(request,'hhands/checkout.html')

class index(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'hhands/index.html', {})

class index_TIBar(View):
        def get(self, request, *args, **kwargs):
            return render(request, 'hhands/index_TIBar.html', {})

# def index_TIBar(request):
#     return render(request,'hhands/index_TIBar.html')


def Med(request):
    # with open('Med.json') as f:
    #     data1 = json.load(f)
    #     print(data1)
    data = [
     {
       "State": "WY",
       "StateName": "Wyoming",
       "DistinctcountofProductName": "2526",
       "Latitude": 43.0001,
       "Longitude": -107.5001,
       "MedicaidAmountReimbursed": "3624748.10",
       "NumberofPrescriptions": "43722",
       "UnitsReimbursed": "2456988.76"
     },
     {
       "State": "WV",
       "StateName": "West Virginia",
       "DistinctcountofProductName": "3182",
       "Latitude": 38.6301,
       "Longitude": -80.7301,
       "MedicaidAmountReimbursed": "591473862.49",
       "NumberofPrescriptions": "9465763",
       "UnitsReimbursed": "1274323269.14"
     }
     ]
    return JsonResponse(data, safe=False)

def usdata(request):
    data = []
    return JsonResponse(data, safe=False)

def physicians(request):
    if request.method == "POST":
        HCP_F_Name = request.POST["HCP_F_Name"]
        HCP_L_Name = request.POST["HCP_L_Name"]
        HCP_Email = request.POST["HCP_Email"]
        HCP_FAX = request.POST["HCP_FAX"]
        Hcp_Info = HcpInformation(f_name = HCP_F_Name, l_name = HCP_L_Name, email = HCP_Email, fax_number = HCP_FAX)

        if HCP_F_Name and HCP_L_Name and HCP_Email and HCP_FAX:
            Hcp_Info.save()
            return InformationSaved(request)
        else:
            print('ERROR FORM INVALID')
    return render(request,'hhands/physicians.html')

def medicaredashboard(request):
    return render(request,'hhands/medicaredashboard.html')

def enrollconfirmation(request):
    return render(request,'hhands/EnrollConfirmation.html')

def customersettings(request):
    data_list = Customers.objects.order_by('c_last_name')
    data_dict = {'c_last_name':data_list}
    return render(request,'hhands/customersettings.html', context=data_dict)

def PhysicianInformation(request):
    data_hcp = HcpInformation.objects.order_by('f_name')
    hcp_dict = {'f_name':data_hcp}
    return render(request,'hhands/PhysicianInformation.html', context=hcp_dict)


def setup(request):
    form = NewCustomerForm()
    if request.method == "POST":
        form = NewCustomerForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return enrollconfirmation(request)
        else:
            print('ERROR FORM INVALID')
    return render(request,'hhands/setup.html', {'form':form})


def customerlogin(request):
    form = NewCustomerLogin()
    if request.method == "POST":
        form = NewCustomerLogin(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return home(request)
        else:
            print('ERROR FORM INVALID')
    return render(request,'hhands/customerlogin.html', {'form':form})


def InformationSaved(request):
    return render(request,'hhands/InformationSaved.html')

def base(request):
    return render(request,'hhands/base.html')

class HcpInformationView(ListView):
    context_object_name = 'hcpinformation'
    model = models.HcpInformation

class HcpInformationDetailView(DetailView):
    context_object_name = 'hcpinfodetails'
    model = models.HcpInformation
    template_name = 'hhands/hcpinfodetails.html'

# class Hcp_dataDetailView(DetailView):
#     context_object_name = 'hcpdatalist'
#     model = models.hcp_data
#     template_name = 'hhands/hcpdatalist.html'

class DrugsHeaderView(ListView):
    # If you don't pass in this attribute,
    # Django will auto create a context name
    # for you with object_list!
    # Default would be 'school_list'

    # Example of making your own:
    context_object_name = 'drugsheader'
    model = models.DrugsHeader

def searchdrugs(request, c_slug=None):
    template_name = 'hhands/drugsheader_list.html'
    c_page = None

    if c_slug!=None:
        c_page = get_object_or_404(Category,slug=c_slug)
        status = models.DrugsHeader.objects.filter(product_name__icontains=drg).order_by(-product_name)
    else:
        if request.method == 'GET':
            drg = request.GET.get('search','')
            status = models.DrugsHeader.objects.filter(product_name__icontains=drg)

    paginator = Paginator(status, 15)
    try:
        page = request.GET.get('page','1')
    except:
        page = 1

    try:
        products = paginator.page(page)

    except (EmptyPage,InvalidPage):
        products = paginator.page(paginator.num_pages)

        return render(request,template_name,{"drg":products})
    else:
        status = 'noresult'
        return render(request,template_name,{"drg":products})


def searchhcp(request, c_slug=None):
    template_name = 'hhands/hcpinformation_list.html'
    c_page = None

    if c_slug!=None:
        c_page = get_object_or_404(Category,slug=c_slug)
        status = models.HcpInformation.objects.filter(l_name__icontains=hcpresults).order_by('-hcp_total_beneficiary_count') | models.HcpInformation.objects.filter(f_name__icontains=hcpresults).order_by('-hcp_total_beneficiary_count') | models.HcpInformation.objects.filter(hcp_zip__icontains=hcpresults).order_by('-hcp_total_beneficiary_count') | models.HcpInformation.objects.filter(speciality__icontains=hcpresults).order_by('-hcp_total_beneficiary_count')
    else:
        if request.method == 'GET':
            hcpresults = request.GET.get('search','')
            status = models.HcpInformation.objects.filter(l_name__icontains=hcpresults).order_by('-hcp_total_beneficiary_count') | models.HcpInformation.objects.filter(f_name__icontains=hcpresults).order_by('-hcp_total_beneficiary_count') | models.HcpInformation.objects.filter(hcp_zip__icontains=hcpresults).order_by('-hcp_total_beneficiary_count') | models.HcpInformation.objects.filter(speciality__icontains=hcpresults).order_by('-hcp_total_beneficiary_count')
        paginator = Paginator(status, 15)
        try:
            page = request.GET.get('page','1')
        except:
            page = 1

        try:
            products = paginator.page(page)

        except (EmptyPage,InvalidPage):
            products = paginator.page(paginator.num_pages)

            return render(request,template_name,{"hcpresults":products})
        else:
            status = {}
            return render(request,template_name,{"hcpresults":products})



def searchhcp_data(request, c_slug=None):
    template_name = 'hhands/hcp_data_list.html'
    c_page = None

    if c_slug!=None:
        c_page = get_object_or_404(Category,slug=c_slug)
        # status = models.hcp_data.objects.filter(L_Name__icontains=hcp_data_results) | models.hcp_data.objects.filter(F_Name__icontains=hcp_data_results)
        status = models.hcp_data.objects.filter(L_Name__icontains=hcp_data_results)
    else:
        if request.method == 'GET':
            hcp_data_results = request.GET.get('search','')
            status = models.hcp_data.objects.filter(L_Name__icontains=hcp_data_results)
            # status = models.hcp_data.objects.filter(L_Name__icontains=hcp_data_results) | models.hcp_data.objects.filter(F_Name__icontains=hcp_data_results)

        paginator = Paginator(status, 15)
        try:
            page = request.GET.get('page','1')
        except:
            page = 1

        try:
            products = paginator.page(page)

        except (EmptyPage,InvalidPage):
            products = paginator.page(paginator.num_pages)

            return render(request,template_name,{"hcp_data_results":products})
        else:
            status = {}
            return render(request,template_name,{"hcp_data_results":products})

class DrugsHeaderDetailView(DetailView):
        context_object_name = 'drugheaderdetails'
        model = models.DrugsHeader
        template_name = 'hhands/drugsdetails.html'

class DrugsHeaderCreateView(CreateView):
    fields = ("product_name", "m_utilization_type", "labeler_code", "product_code", "package_size")
    model = models.DrugsHeader

class DrugsHeaderUpdateView(UpdateView):
    fields = ("m_utilization_type", "labeler_code", "product_code", "package_size", "product_name")
    model = models.DrugsHeader

class DrugsHeaderDeleteView(DeleteView):
    model = models.DrugsHeader
    success_url = reverse_lazy("hhands:drugs")

# below class for braintree
class CheckoutView(generic.FormView):
    """This view lets the user initiate a payment."""
    form_class = forms.CheckoutForm
    template_name = 'hhands/checkout.html'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        # We need the user to assign the transaction
        self.user = request.user

        # Ha! There it is. This allows you to switch the
        # Braintree environments by changing one setting
        if settings.BRAINTREE_PRODUCTION:
            braintree_env = braintree.Environment.Production
        else:
            braintree_env = braintree.Environment.Sandbox

        # Configure Braintree
        braintree.Configuration.configure(
            braintree_env,
            merchant_id=settings.BRAINTREE_MERCHANT_ID,
            public_key=settings.BRAINTREE_PUBLIC_KEY,
            private_key=settings.BRAINTREE_PRIVATE_KEY,
        )

        # Generate a client token. We'll send this to the form to
        # finally generate the payment nonce
        # You're able to add something like ``{"customer_id": 'foo'}``,
        # if you've already saved the ID
        self.braintree_client_token = braintree.ClientToken.generate({})
        return super(CheckoutView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        ctx = super(CheckoutView, self).get_context_data(**kwargs)
        ctx.update({
            'braintree_client_token': self.braintree_client_token,
        })
        return ctx

    def form_valid(self, form):
        # Braintree customer info
        # You can, for sure, use several approaches to gather customer infos
        # For now, we'll simply use the given data of the user instance
        customer_kwargs = {
            "first_name": self.user.first_name,
            "last_name": self.user.last_name,
            "email": self.user.email,
        }

        # Create a new Braintree customer
        # In this example we always create new Braintree users
        # You can store and re-use Braintree's customer IDs, if you want to
        result = braintree.Customer.create(customer_kwargs)
        if not result.is_success:
            # Ouch, something went wrong here
            # I recommend to send an error report to all admins
            # , including ``result.message`` and ``self.user.email``

            context = self.get_context_data()
            # We re-generate the form and display the relevant braintree error
            context.update({
                'form': self.get_form(self.get_form_class()),
                'braintree_error': u'{} {}'.format(
                    result.message, _('Please get in contact.'))
            })
            return self.render_to_response(context)

        # If the customer creation was successful you might want to also
        # add the customer id to your user profile
        customer_id = result.customer.id

        """
        Create a new transaction and submit it.
        I don't gather the whole address in this example, but I can
        highly recommend to do that. It will help you to avoid any
        fraud issues, since some providers require matching addresses

        """
        address_dict = {
            "first_name": self.user.first_name,
            "last_name": self.user.last_name,
            "street_address": 'street',
            "extended_address": 'street_2',
            "locality": 'city',
            "region": 'state_or_region',
            "postal_code": 'postal_code',
            "country_code_alpha2": 'alpha2_country_code',
            "country_code_alpha3": 'alpha3_country_code',
            "country_name": 'country',
            "country_code_numeric": 'numeric_country_code',
        }

        # You can use the form to calculate a total or add a static total amount
        # I'll use a static amount in this example
        result = braintree.Transaction.sale({
            "customer_id": customer_id,
            "amount": 100,
            "payment_method_nonce": form.cleaned_data['payment_method_nonce'],
            "descriptor": {
                # Definitely check out https://developers.braintreepayments.com/reference/general/validation-errors/all/python#descriptor
                "name": "COMPANY.*test",
            },
            "billing": address_dict,
            "shipping": address_dict,
            "options": {
                # Use this option to store the customer data, if successful
                'store_in_vault_on_success': True,
                # Use this option to directly settle the transaction
                # If you want to settle the transaction later, use ``False`` and later on
                # ``braintree.Transaction.submit_for_settlement("the_transaction_id")``
                'submit_for_settlement': True,
            },
        })
        if not result.is_success:
            # Card could've been declined or whatever
            # I recommend to send an error report to all admins
            # , including ``result.message`` and ``self.user.email``
            context = self.get_context_data()
            context.update({
                'form': self.get_form(self.get_form_class()),
                'braintree_error': _(
                    'Your payment could not be processed. Please check your'
                    ' input or use another payment method and try again.')
            })
            return self.render_to_response(context)

        # Finally there's the transaction ID
        # You definitely want to send it to your database
        transaction_id = result.transaction.id
        # Now you can send out confirmation emails or update your metrics
        # or do whatever makes you and your customers happy :)
        return super(CheckoutView, self).form_valid(form)

    def get_success_url(self):
        # Add your preferred success url
        return reverse('foo')
