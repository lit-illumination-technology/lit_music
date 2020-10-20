import math
from . import _singleton_music_analyzer

name = "Music Bands"

start_string = name + " started!"

description = "Changes color and brightness with music"

schema = {}
schema.update(_singleton_music_analyzer.music_vis_schema)

def update(lights, step, state):
    app = state[_singleton_music_analyzer.MUSIC_VIS_FIELD]
    lights_per_band = lights.size / len(app.bands)
    for i, band in enumerate(app.bands):
        color_h = float(i)/len(app.bands)
        for n in range(int(lights_per_band * i), int(lights_per_band * (i + 1))):
            val = 1/(1+math.exp(-(10*(band/1023)-7)))
            lights.set_pixel_hsv(n, color_h, 1, val)
