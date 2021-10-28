clean:
	rm -rf build dist

build-dev:
	python setup.py py2app -A

build-prod:
	python setup.py py2app

run:
	open dist/groove.app
