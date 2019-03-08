"""
This holds a set of constant variables for qute
"""
import os
import logging

log = logging.getLogger('qute')


# -- This is the name of the environment variable we will
# -- check for
QUTE_STYLE_PATH = 'QUTE_STYLE_PATH'

# -- This will look at the environment variable for styles and pull
# -- out a resolved list of those locations which exist
QUTE_STYLE_LOCATIONS = [
    location
    for location in os.environ.get(
        QUTE_STYLE_PATH,
        ''
    ).split(';')
    if os.path.exists(location)
]

QUTE_STYLE_LOCATIONS.insert(
    0,
    os.path.join(
        os.path.dirname(__file__),
        'styles',
    ),
)

# -- This is a set of default variables used when
# -- applying style sheets
STYLE_DEFAULTS = {
    '_BACKGROUND_': '30, 30, 30',
    '_ALTBACKGROUND_': '70, 70, 70',
    '_FOREGROUND_': '176, 224, 7',
    '_HIGHLIGHT_': '250, 255, 50',
    '_TEXT_': '255, 255, 255',
}
