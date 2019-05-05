from django import forms
from hhands.models import Customers, CustomerLogin, HcpInformation
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from django import forms
from django.utils.translation import ugettext_lazy as _


class UserSignUpForm(UserCreationForm):
    class Meta:
        fields = ('username', 'email','password1','password2')
        model = get_user_model()

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['username'].label = 'Display Name'
        self.fields['email'].label = 'Email Address'



class NewCustomerForm(forms.ModelForm):
    class Meta():
        model = Customers
        fields = '__all__'


class NewCustomerLogin(forms.ModelForm):
    class Meta():
        model = CustomerLogin
        fields = '__all__'
        #fields = customer_user_name

class CheckoutForm(forms.Form):
    payment_method_nonce = forms.CharField(
        max_length=1000,
        widget=forms.widgets.HiddenInput,
        required=True,  # In the end it's a required field, but I wanted to provide a custom exception message
    )

    def clean(self):
        self.cleaned_data = super(CheckoutForm, self).clean()

        # Braintree nonce is missing
        if not self.cleaned_data.get('payment_method_nonce'):
            raise forms.ValidationError(_(
                'We couldn\'t verify your payment. Please try again.'))
        return self.cleaned_data
