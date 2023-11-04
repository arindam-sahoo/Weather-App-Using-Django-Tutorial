from django import forms

class CityForm(forms.Form):
    city = forms.CharField(label='Enter a city', max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
