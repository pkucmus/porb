# encoding: utf-8

from django import forms


class CheckoutForm(forms.Form):
    product_id = forms.IntegerField(required=True, widget=forms.HiddenInput())
    acceptance = forms.BooleanField(label='Akceptuję regulamin', required=True)

    address = forms.CharField(
        label='Dane do wysyłki', required=True, widget=forms.Textarea()
    )
