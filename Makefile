.PHONY: typehint
typehint:
	mypy --ignore-missing-imports src/

.PHONY: lint
lint:
	pylint --load-plugins pylint_django --disable=C0114 src/

.PHONY: checklist
	checklist: lint typehint

.PHONY: black
black:
	black -l 79 src/*.py

.PHONY: clean
clean:
	find . -type f -name "*.pyc" | xargs rm -fr
	find . -type d -name __pycache__ | xargs rm -fr
