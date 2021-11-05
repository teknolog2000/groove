clean:
	rm -rf build dist

build-dev: dependencies
	python3 setup.py py2app -A
	open dist

build: dependencies
	python3 setup.py py2app
	open dist

dependencies:
	pip install -r requirements.txt

run:
	open dist/groove.app
