.PHONY: clean build-dev build run

clean:
	rm -rf build dist

build-dev:
	uv run setup.py py2app -A
	open dist

build:
	uv run setup.py py2app
	open dist

run:
	open dist/groove.app
