from action.path.hbo import HboPath
from action.path.youtube import YouTube

def _pathButtons():
    return {
        'hbo': HboPath('hbo', 'https://play.hbomax.com/'),
        'youtube': YouTube('youtube', 'https://youtube.com/'),
    }