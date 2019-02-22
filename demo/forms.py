import django.forms as forms


class InterestForm(forms.Form):
    amount = forms.IntegerField(label="Deposit Amount")
    period = forms.IntegerField(label="Deposit Period(Months)")
