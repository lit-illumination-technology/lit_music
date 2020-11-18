import colorsys
import random

from . import _singleton_music_analyzer

name = "Music Cycle"

start_message = name + " started!"

description = "Cycles color and changes brightness with music"

schema = {
}
schema.update(_singleton_music_analyzer.music_vis_schema)


MIN_BRIGHTNESS = 0.1
def update(lights, step, state):
    app = state[_singleton_music_analyzer.MUSIC_VIS_FIELD]
    vol = (app.bands[0] / 1023)

    hsv = [(step/500)%1, 1, vol]

    lights.set_all_pixels_hsv(*hsv)
