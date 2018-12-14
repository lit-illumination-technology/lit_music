import math
from . import _singleton_music_analyzer

name = "Music Dots"

start_string = name + " started!"

description = "Changes color and brightness with music"

schema = {}
schema.update(_singleton_music_analyzer.music_vis_schema)

def update(lights, step, state):
    app = state[_singleton_music_analyzer.MUSIC_VIS_FIELD]
    inverse_total_brightness = 1-(1/(1+math.exp(-(10*(app.total_volume/(1023*app.num_bands))-1))))
    for n in range(0, lights.num_leds, len(app.bands)+1):
        lights.set_pixel_hsv(n, 1, 0, inverse_total_brightness)
    for i, band in enumerate(app.bands):
        color_h = float(i)/len(app.bands)
        val = 1/(1+math.exp(-(10*(band/1023)-7)))
        for n in range(i+1, lights.num_leds, len(app.bands)+1):
            lights.set_pixel_hsv(n, color_h, 1, val)
