# encoding: utf-8

from django import forms


class CheckoutForm(forms.Form):
    acceptance = forms.BooleanField(label='Akceptuję regulamin', required=True)

    name = forms.CharField(
        label='imię nazwisko', required=True,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    address_line_1 = forms.CharField(
        label='ulica', required=True,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    city = forms.CharField(
        label='miasto', required=True,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    post_code = forms.RegexField(
        regex='[0-9]{2}-[0-9]{3}',
        label='kod-pocztowy', required=True,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    email = forms.EmailField(
        label='e-mail', required=True,
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
