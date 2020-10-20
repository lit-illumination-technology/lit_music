import math

from . import _singleton_music_analyzer

name = "Music Expand"

start_string = name + " started!"

description = "Changes color with music"

schema = {}
schema.update(_singleton_music_analyzer.music_vis_schema)

def update(lights, step, state):
    app = state[_singleton_music_analyzer.MUSIC_VIS_FIELD]
    center = lights.size / 2
    hues = [(1, 0)]*lights.size
    bands = [app.bands[0], (app.bands[1] + app.bands[2] + app.bands[3])/3, (app.bands[4] + app.bands[5] + app.bands[6])/3]
    for i, band in enumerate(bands):
        color_h = i/len(bands)
        val = (1/(1+math.exp(-(10*(band/1023)-7))))*(lights.size/2)
        for n in range(int(center-val), int(center+val)):
            h, s = hues[n]
            hues[n] = (h*color_h, s+1)
    lights.clear()
    for n, (h, s) in enumerate(hues):
        if s is not 0:
            lights.set_pixel_hsv(n, h, 1, 1)
