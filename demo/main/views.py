from django.views.generic import FormView
from django.http import HttpResponse
from ratelimit9.mixins import Ratelimit9Mixin
from main.forms import MyForm

class MyView(Ratelimit9Mixin, FormView):
	template_name = 'main/form.html'
	form_class = MyForm
	success_url = '/sent'
	ratelimit_key = 'ip'
	ratelimit_rate = '3/m'
	
	def form_valid(self, form):
		return HttpResponse('Form has been successfully sent.')