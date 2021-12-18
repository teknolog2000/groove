clean:
	rm -rf build dist

build-dev: dependencies
	python3 setup.py py2app -A
	open dist

build: dependencies
	python3 setup.py py2app
	open dist

dependencies:
	pip3 install -r requirements.txt

run:
	open dist/groove.app
