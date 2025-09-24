from redis import StrictRedis
from time import strftime, sleep
from action.organizer import _pathButtons
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
                direction = data['path'].split('-')[1]
                posX, posY = pyautogui.position()
                
                print(posX, posY)
                
                if posY<=250:
                    pyautogui.scroll(+3)
                    pyautogui.moveTo(posX, posY+300)
                    continue
                
                if direction == 'up':
                    pyautogui.moveTo(posX, posY-100)
                
                if direction == 'down':
                    pyautogui.moveTo(posX, posY+100)
                
                if direction == 'left':
                    pyautogui.moveTo(posX-100, posY)
                
                if direction == 'right':
                    pyautogui.moveTo(posX+100, posY)
                
                if posY>=650:
                    pyautogui.scroll(-3)
                    pyautogui.moveTo(posX, posY-300)
                    continue
                
                continue
            
            if not data['path'] in _pathButtons():
                print(f'Atalho "{data['path']}" não registrado')
                continue
            
            classInstance = _pathButtons()[data['path']]
            classInstance.run()
            
        elif 'url' in data:
            webbrowser.open(data['url'])