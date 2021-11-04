# Groove

A Mac OS status bar app for playing ambient beats while I work. I wanted a minimal UI to turn on and off the stream.

Currently supports these streams

*  [Groove Salad from SomaFM](https://somafm.com/groovesalad/)
* [Chillsky](https://www.chillsky.com)

![Screenshot](/screenshot.png)

## Building

Groove uses libVLC to play the stream, so it requires the [VLC](https://www.videolan.org) player to be installed.

Then build using
```bash
> python3 -m venv venv
> source venv/bin/activate
> pip3 install -r requirements.txt
> make build-prod
``` 
and you'll find `groove.app` in the `dist` directory.
