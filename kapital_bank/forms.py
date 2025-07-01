from django import forms
from .models import KapitalBank

class KapitalBankForm(forms.ModelForm):
    class Meta:
        model = KapitalBank
        fields = '__all__'  # Və ya lazım olan sahələri ayrıca yaza bilərsən, məsələn: ['user', 'receiver', 'amount', 'status']
