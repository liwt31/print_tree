.PHONY: format, test

format:
	black .

publish:
	rm -rf dist/
	python setup.py sdist bdist_wheel
	twine upload -s dist/*

test:
	pytest
