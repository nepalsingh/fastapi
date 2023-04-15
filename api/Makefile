install:
	# install dependencies
	pip install --upgrade pip && \
		pip install -r requirements.txt
format:
	# format code
	black .
lint:
	# lint code
	flake8 --ignore=E501,F401,W503 app
test:
	# test all cases

run:
	# run the API
	python app/main.py	

all:
	# install, format, lint and test
	install format lint test
