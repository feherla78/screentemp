from setuptools import setup

setup(
    name="screentemp",
    version="0.1.0",
    packages=["screentemp"],
    install_requires=[
        "PyGObject",
    ],
    entry_points={
        "console_scripts": [
            "screentemp = screentemp.main:main",
        ],
    },
    data_files=[
    ('/usr/share/applications', ['data/applications/screentemp.desktop']),
    ('/usr/share/icons/hicolor/48x48/apps', ['data/icons/hicolor/48x48/apps/screentemp.png']),
    ('/usr/share/icons/hicolor/64x64/apps', ['data/icons/hicolor/64x64/apps/screentemp.png']),
    ('/usr/share/icons/hicolor/128x128/apps', ['data/icons/hicolor/128x128/apps/screentemp.png']),
    ('/usr/share/icons/hicolor/256x256/apps', ['data/icons/hicolor/256x256/apps/screentemp.png']),
    ],

)