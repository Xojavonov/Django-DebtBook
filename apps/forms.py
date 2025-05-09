
from django.forms.models import ModelForm

from apps.models import DebtBook


# ===========================================================Debt=====================
class DebtModelFormCreate(ModelForm):
    class Meta:
        model = DebtBook
        fields = 'name', 'number', 'debt'


class DebtModelFormUpdate(ModelForm):
    class Meta:
        model = DebtBook
        fields = ['debt']


