# encoding: utf-8
from django import forms

from products.models import Category


def make_category_choices():
    return tuple(
        {
            category.name: [
                (subcategory.pk, subcategory.name, )
                for subcategory in category.sub_categories.all()
            ] for category in Category.objects.filter(
                sub_categories__isnull=False
            )
        }.iteritems()
    ) + tuple([
        (category.pk, category.name)
        for category in Category.objects.filter(
            sub_categories__isnull=True, parent__isnull=True
        )
    ]) + ((None, 'Wszystkie kategorie', ), )


class SearchForm(forms.Form):
    name = forms.CharField(
        required=False, widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'nazwa, część nazwy lub opisu'
            }
        )
    )
    categories = forms.ChoiceField(
        choices=make_category_choices(), required=False, widget=forms.Select(
            attrs={'class': 'form-control'}
        )
    )
    price_from = forms.DecimalField(
        label='cena od', widget=forms.NumberInput(
            attrs={'class': 'form-control', 'placeholder': 'cena od'}
        )
    )
    price_to = forms.DecimalField(
        label='cena do', widget=forms.NumberInput(
            attrs={'class': 'form-control', 'placeholder': 'cena do'}
        )
    )
