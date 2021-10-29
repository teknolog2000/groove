clean:
	rm -rf build dist

build-dev:
	python3 setup.py py2app -A

build-prod:
	python3 setup.py py2app

run:
	open dist/groove.app
