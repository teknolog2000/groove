from setuptools import setup

APP = ['groove.py']
DATA_FILES = ['play.png', 'stop.png']
OPTIONS = {
    'argv_emulation': True,
    'plist': {
        'CFBundleShortVersionString': '0.1.0',
        'LSUIElement': True,
    },
    'iconfile': 'groove.icns',
    'packages': ['rumps'],
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
