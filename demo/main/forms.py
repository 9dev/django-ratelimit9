from django.forms import Form
from ratelimit9.forms import Ratelimit9Form

class MyForm(Ratelimit9Form, Form):
    name = forms.CharField()