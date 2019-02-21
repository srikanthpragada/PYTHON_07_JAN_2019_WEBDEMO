import django.forms as forms


class InterestForm(forms.Form):
    amount = forms.IntegerField()
    period = forms.IntegerField()
