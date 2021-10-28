import rumps
import vlc

URL = 'https://ice4.somafm.com/groovesalad-128-mp3'

rumps.debug_mode(True)


class GrooveApp(rumps.App):
    def __init__(self, name):
        super(GrooveApp, self).__init__(
            'Groove App', icon='icon.png', template=True)
        self.player = vlc.MediaPlayer(URL)
        self.player.play()

    @rumps.clicked("Play")
    def onoff(self, sender):
        print('heyo')
        sender.state = not sender.state
        if sender.state:
            rumps.notification("Groove App", "Playing", "message")
            self.player.play()
        else:
            self.player.stop()


if __name__ == "__main__":
    GrooveApp("Groove App").run()
