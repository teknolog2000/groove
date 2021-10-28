import rumps
import vlc

STREAM_URL = 'https://ice4.somafm.com/groovesalad-128-mp3'


class GrooveApp(rumps.App):
    def __init__(self, name):
        super(GrooveApp, self).__init__('Groove App', icon='stop.png', template=True)
        self.player = vlc.MediaPlayer(STREAM_URL)

        self.events = self.player.event_manager()
        self.events.event_attach(vlc.EventType.MediaPlayerPlaying, self.vlc_event)
        self.events.event_attach(vlc.EventType.MediaPlayerStopped, self.vlc_event)

    def vlc_event(self, event):
        playing = event.type == vlc.EventType.MediaPlayerPlaying

        self.icon = 'play.png' if playing else 'stop.png'
        self.menu['Play'].state = playing

    # i haven't found a better way to set the initial menu state to -1
    @rumps.timer(0.1)
    def timeout(self, sender):
        sender.stop()
        self.menu['Play'].state = -1
        self.player.play()

    @rumps.clicked('Play')
    def play(self, sender):
        if sender.state == 0:
            sender.state = -1
            self.player.play()
        elif sender.state == 1:
            self.player.stop()


if __name__ == '__main__':
    GrooveApp('Groove').run()
