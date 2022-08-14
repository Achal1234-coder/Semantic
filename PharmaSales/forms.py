from django import forms

class Pharma(forms.Form):
    year = forms.IntegerField()
    drug_classification = forms.CharField()
