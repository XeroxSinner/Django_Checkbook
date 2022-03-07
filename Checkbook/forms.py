from django.forms import ModelForm
from .models import Accounts, Transaction

class AccountForm(ModelForm):
    class Meta:
        model = Accounts
        fields = '__all__'
        
class TransactionForm(ModelForm):
    class Meta:
        model = Transaction
        fields = '__all__'
        
