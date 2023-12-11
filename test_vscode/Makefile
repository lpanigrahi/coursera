test:
	python -m unittest discover -s tests -p '*_test.py'

format:
	black *.py tests/*.py

lint:
	pylint --disable=R,C --extension-pkg-whitelist=pydantic *.py tests/*.py

container-lint:
	docker run --rm -v $(PWD):/app -w /app hadolint/hadolint hadolint Dockerfile

refactor:
	# Refactor code to use f-strings
	refactor -f f-string *.py tests/*.py

deploy:
	# Deploy to PyPi
	python setup.py sdist bdist_wheel
	twine upload dist/*