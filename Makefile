run:
	python manage.py runserver

migrations:
	python manage.py makemigrations

migrate:
	python manage.py migrate

test:
	pytest -vv . apps/

statics:
	python manage.py collectstatic --noinput

format:
	isort -rc apps/
	black apps/