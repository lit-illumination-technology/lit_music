from music_visualization_framework import music_analyzer

MUSIC_VIS_FIELD = '_singleton_music_vis'

def create_music_analyzer(controller):
    app = music_analyzer.Analyzer("/dev/ttyACM0")
    app.start()
    return app

music_vis_schema = {
    MUSIC_VIS_FIELD: {
        'value': {
            'type': 'music_analyzer',
            'default_gen': create_music_analyzer
        },
        'user_input': False,
        'singleton': True
    }
}
