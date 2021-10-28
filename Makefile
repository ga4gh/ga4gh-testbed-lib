Nothing:
	@echo "No target provided. Stop"

.PHONY: install
install:
	@python setup.py install

.PHONY: build
build:
	@python setup.py sdist bdist_wheel

.PHONY: upload-pypi-test
upload-pypi-test:
	@twine upload --repository-url https://test.pypi.org/legacy/ dist/*

.PHONY: upload-pypi
upload-pypi:
	@twine upload dist/*