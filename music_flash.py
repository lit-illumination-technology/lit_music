import colorsys
import math

from . import _singleton_music_analyzer

name = "Music Flash"

start_string = name + " started!"

description = "Changes color and brightness with music"

schema = {
    'color': {
        'value': {
            'type': 'color',
            'default': (255, 255, 255)
        },
        'user_input': False
    }
}
schema.update(_singleton_music_analyzer.music_vis_schema)

MIN_BRIGHTNESS = 0.3
def update(lights, step, state):
    app = state[_singleton_music_analyzer.MUSIC_VIS_FIELD]
    if app.total_volume_beat:
        state['color'] = tuple([int(255*x) for x in colorsys.hsv_to_rgb(random.random(), 1, 1)])
        #color=(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        vol = 1
    elif state['color'] is None:
        state['color'] = (255, 255, 255)
    else:
        #vol = math.sqrt((app.total_volume / (1023 *  app.num_bands)))
        #vol = (app.total_volume / (1023 *  app.num_bands))
        vol = (app.bands[0] / 1023)
        #vol = (1 - MIN_BRIGHTNESS) * np.tanh((app.total_volume / (1023 *  app.num_bands))) + MIN_BRIGHTNESS

    display_color = tuple([int(vol*x) for x in state['color']])
    lights.set_all_pixels(*display_color)
