from redis import StrictRedis
from time import strftime, sleep
from action.organizer import _pathButtons
from action.desktop.mouse import  Mouse
import pyautogui
import webbrowser
import json

# https://dev.to/felipepaz/python-e-redis-utilizando-pubsub-51fo

client = StrictRedis(host="localhost", port=6379)

subscriber = client.pubsub()
subscriber.psubscribe('channel_test')

while True:
    messages = subscriber.get_message()

    if messages:
        data = messages["data"]
        
        if str(data) == '1': continue
        data = json.loads(data)

        if 'path' in data:
            if 'mouse' in data['path']:
                Mouse(data)._control_()
                continue
            
            if not data['path'] in _pathButtons():
                print(f'Atalho "{data['path']}" não registrado')
                continue
            
            classInstance = _pathButtons()[data['path']]
            classInstance.run()
            
        elif 'url' in data:
            webbrowser.open(data['url'])