.DEFAULT_GOAL := all

all: install test run deploy

install:
	@echo "Installing pipenv and dependencies."
	pip3 install pipenv
	pipenv --python 3.8
	pipenv install requests
	pipenv install ntplib
	pipenv install pytest
test:
	@echo "Start tests."
	pipenv run pytest tests/tests.py >> results.txt
run:
	@echo "Run Python app."
	pipenv run python3 app.py >> results.txt

deploy:
	@echo "Adding and Committing results.txt to git."
	git add .
	git commit -m "Lab2: автоматичне оновлення через make"
	git push
