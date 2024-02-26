from django import forms

from .models import Coupon


class DiscountCodeForm(forms.ModelForm):
    class Meta:
        model = Coupon
        fields = '__all__'