from django import forms
from django.conf import settings

from .helpers import SPGATEWAY_API_VERSION as api_version


class SpgatewayForm(forms.Form):
    MerchantID = forms.CharField(max_length=15, widget=forms.HiddenInput())
    TradeInfo = forms.CharField(widget=forms.HiddenInput())
    TradeSha = forms.CharField(widget=forms.HiddenInput())
    Version = forms.CharField(max_length=5, initial=api_version, widget=forms.HiddenInput())
    action = 'https://ccore.newebpay.com/MPG/mpg_gateway' if settings.DEBUG else 'https://core.newebpay.com/MPG/mpg_gateway'
