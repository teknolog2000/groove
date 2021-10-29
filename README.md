# Groove

A Mac OS status bar app for playing SomaFM's [Groove Salad](https://somafm.com/groovesalad/) stream - which they describe as _A nicely chilled plate of ambient/downtempo beats and grooves._ I like to listen to this while I work.

There is already the more complete [SomaFM Radio Player](https://apps.apple.com/us/app/somafm-radio-player/id449155338?mt=12) app, but I wanted a minimal UI to turn on and off this one stream.

![Screenshot](/screenshot.png)

## Building

Groove uses libVLC to play the stream, so it requires the [VLC](https://www.videolan.org) player to be installed.

Then build using
```bash
> python3 -m venv venv
> source venv/bin/activate
> pip install -r requirements
> make build-prod
``` 
and you'll find `groove.app` in the `dist` directory.
