from .models import Transaction
from django import forms
class TransactionAdd(forms.ModelForm):
    CHOICES = [('borrow', '借入'), ('buy', '仕入')]
    transaction_category =  forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)
    class Meta:
        model = Transaction
        fields = ['transaction_category','trading_partner','amount']
