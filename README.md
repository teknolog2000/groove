# Groove

A Mac OS status bar app for playing ambient beats while I work. I wanted a minimal UI to turn on and off the stream.

Currently supports these streams

*  [Groove Salad from SomaFM](https://somafm.com/groovesalad/)
* [Chillsky](https://www.chillsky.com)

![Screenshot](/screenshot.png)

## Installing

Groove is built with Python, and uses [py2app](https://py2app.readthedocs.io/en/latest/) to turn it into a Mac .app executable. There is no pre-built and signed binary, so you'll have to build it locally yourself.

### Get dependencies
You'll need Python3, which you can get [from python.org](https://www.python.org/downloads/) (although I prefer to use use [Homebrew](https://brew.sh) to install it.

Groove uses libVLC to play the stream, so it requires the [VLC player](https://www.videolan.org)to be installed.

### Build
Then build using
```bash
> pip3 install -r requirements.txt
> make build-prod
``` 
and you'll find `groove.app` in the `dist` directory.

### Install
Just do
```bash
> open dist
```
then drag `groove.app` to your Applications folder.
