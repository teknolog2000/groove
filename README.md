# Groove

A Mac OS status bar app for playing ambient beats while I work. I wanted a minimal UI to turn on and off the stream.

Currently supports these streams

*  [Groove Salad from SomaFM](https://somafm.com/groovesalad/)
* [Chillsky](https://www.chillsky.com)

![Screenshot](/screenshot.png)

## Installing

Groove is built with Python, and uses [py2app](https://py2app.readthedocs.io/en/latest/) to turn it into a Mac .app executable. There is no pre-built and signed binary, so you'll have to build it locally yourself.

### Get dependencies
You'll need these dependencies to build

* [Python 3](https://www.python.org/downloads/)
* [VLC player](https://www.videolan.org) which provides libVLC

### Build
Then build using
```bash
> make build
``` 
and you'll find `groove.app` in the `dist` directory.

### Install
It's a Mac app, so just drag `groove.app` to your Applications folder.
