setup-environment:
	pip3 install virtualenv==20.0.15
	virtualenv env
	source env/bin/activate; \
	pip3 install -r requirements.txt

format:
	@echo Formatting...
	source env/bin/activate; \
	python -m black .

lint: format
	@echo Linting...
	source env/bin/activate; \
	python -m flake8 .