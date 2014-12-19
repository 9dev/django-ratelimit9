
ENVIRONMENT = development
PROJECT_NAME = demo
PYTHON_COMMAND = python2.7
VENV_PATH = ./virtualenv/demo

#####

default:
	$(MAKE) run

install:
	$(MAKE) upgrade
	$(MAKE) syncdb
	$(MAKE) createadmin

#####

run:
	( \
		. $(VENV_PATH)/bin/activate; \
		$(PYTHON_COMMAND) manage.py runserver localhost:8000; \
	)

upgrade:
	( \
		. $(VENV_PATH)/bin/activate; \
		pip install -r requirements.txt; \
	)

syncdb:
	( \
		. $(VENV_PATH)/bin/activate; \
		$(PYTHON_COMMAND) manage.py syncdb --noinput; \
	)

test:
	( \
		. $(VENV_PATH)/bin/activate; \
		$(PYTHON_COMMAND) manage.py test main; \
		$(PYTHON_COMMAND) manage.py test ratelimit9; \
	)

reinstall:
	( \
		. $(VENV_PATH)/bin/activate; \
		$(PYTHON_COMMAND) manage.py sqlclear main | $(PYTHON_COMMAND) manage.py dbshell; \
		$(PYTHON_COMMAND) manage.py sqlclear ratelimit9 | $(PYTHON_COMMAND) manage.py dbshell; \
	)
	$(MAKE) syncdb

createadmin:
	( \
		. $(VENV_PATH)/bin/activate; \
		echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'admin')" | $(PYTHON_COMMAND) manage.py shell; \
	)

