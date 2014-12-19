from django import forms
from ratelimit9.forms import Ratelimit9Form

class MyForm(Ratelimit9Form, forms.Form):
    name = forms.CharField()