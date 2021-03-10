dev_setup:
	pip install -r requirements.txt
	brew list geckodriver || HOMEBREW_NO_AUTO_UPDATE=1 brew install geckodriver

test:
	python manage.py test tests

test_e2e:
	python manage.py test e2e.local

migrate:
	python manage.py migrate

runserver:
	python manage.py runserver localhost:8000

rundemo:
	./demo.sh