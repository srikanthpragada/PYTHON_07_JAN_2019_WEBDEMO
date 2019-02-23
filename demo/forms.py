import django.forms as forms
from django.forms import ModelForm
from .models import Title


class InterestForm(forms.Form):
    amount = forms.IntegerField(label="Deposit Amount")
    period = forms.IntegerField(label="Deposit Period(Months)")


class TitleForm(ModelForm):
    class Meta:
       model = Title
       fields = '__all__'