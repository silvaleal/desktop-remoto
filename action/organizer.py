from action.applications.hbo import HboPath
from action.applications.youtube import YouTube

def _pathButtons():
    return {
        'hbo': HboPath('https://play.hbomax.com/'),
        'youtube': YouTube('https://youtube.com/'),
    }