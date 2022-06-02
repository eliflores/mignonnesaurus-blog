dev_setup:
	brew list geckodriver || HOMEBREW_NO_AUTO_UPDATE=1 brew install geckodriver
	pipenv shell
	pipenv install

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
