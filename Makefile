mig:
	python3 manage.py makemigrations
upg:
	python3 manage.py migrate
admin:
	 python3 manage.py  createsuperuser
start:
	 python3 manage.py startapp  todo
