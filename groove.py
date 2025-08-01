import rumps
import vlc

DEFAULT_STREAM = 'Groove Salad'

STREAMS = {
    DEFAULT_STREAM: 'https://ice2.somafm.com/groovesalad-64-aac',
    'Chillsky': 'https://chill.radioca.st/stream'
}


# rumps.debug_mode(True)


class GrooveApp(rumps.App):
    def __init__(self, name):
        self.player = None

        menu = [rumps.MenuItem(s, callback=self.menu_click) for s in STREAMS]
        menu.append(None)
        super(GrooveApp, self).__init__('Groove App', menu=menu, icon='stop.png', template=True)

    def vlc_event(self, event, stream_name):
        playing = event.type == vlc.EventType.MediaPlayerPlaying

        self.icon = 'play.png' if playing else 'stop.png'

        for m in self.menu:
            # need to ignore the separator
            if type(self.menu[m]) != rumps.MenuItem:
                continue

            self.menu[m].state = playing and self.menu[m].title == stream_name

    # i haven't found a better way to set the initial menu state to -1
    @rumps.timer(0.1)
    def timeout(self, sender):
        sender.stop()

        for m in STREAMS:
            self.menu[m].state = -1

        self.start_stream(DEFAULT_STREAM)

    def menu_click(self, sender):
        if sender.state == 0:
            sender.state = -1
            self.start_stream(sender.title)
        elif sender.state == 1:
            self.player.stop()

    def start_stream(self, stream_name):
        if self.player:
            self.player.stop()

        self.player = vlc.MediaPlayer(STREAMS[stream_name])

        self.events = self.player.event_manager()
        self.events.event_attach(vlc.EventType.MediaPlayerPlaying, self.vlc_event, stream_name)
        self.events.event_attach(vlc.EventType.MediaPlayerStopped, self.vlc_event, stream_name)

        self.player.play()


if __name__ == '__main__':
    GrooveApp('Groove').run()
