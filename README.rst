*****************
django-ratelimit9
*****************

``django-ratelimit9`` combines `django-recaptcha <https://github.com/praekelt/django-recaptcha>`_ and `django-ratelimit <https://github.com/jsocol/django-ratelimit>`_ into a single app.

Each time when a limit is exceeded a reCAPTCHA field is dynamically appended to a Form.  

Make sure you have read the docs of these two requirements in order to learn how to set up limits and customize the reCAPTCHA.

Requirements
============

- `django-recaptcha <https://github.com/praekelt/django-recaptcha>`_

- `django-ratelimit <https://github.com/jsocol/django-ratelimit>`_

Installation
============

- Install via pip::

    pip install django-ratelimit9

- Add ``ratelimit9`` to your ``INSTALLED_APPS``

Usage
=====

Let's say you want to use view ``MyView`` along with ``MyForm`` form.

Code for your ``forms.py``::

	from django.forms import Form
	from ratelimit9.forms import Ratelimit9Form
	
	class MyForm(Ratelimit9Form, ModelForm):
		# ...

Code for your ``views.py``::

	from django.views.generic import CreateView
	from ratelimit9.mixins import Ratelimit9Mixin
	
	class MyView(Ratelimit9Mixin, CreateView):
		ratelimit_key = 'ip'
		ratelimit_rate = '5/m'
		# ...
