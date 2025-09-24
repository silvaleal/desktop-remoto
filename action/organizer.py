from action.path.hbo import HboPath
from action.path.youtube import YouTube

def _pathButtons():
    return {
        'hbo': HboPath('https://play.hbomax.com/'),
        'youtube': YouTube('https://youtube.com/'),
    }