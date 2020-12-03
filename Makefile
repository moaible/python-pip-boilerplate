setup:
	pipenv install
	pipenv install -d
install:
	pip install git+https://github.com/moaible/python-pip-executable-boilerplate
uninstall:
	pip uninstall executable-boilerplate -y
reinstall: uninstall install
lint:
	pipenv run vet
autocorrect:
	pipenv run fmt
test:
	pipenv run test
