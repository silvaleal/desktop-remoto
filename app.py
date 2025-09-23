from redis import StrictRedis
from time import strftime, sleep
from action.organizer import _pathButtons
import json

# https://dev.to/felipepaz/python-e-redis-utilizando-pubsub-51fo

client = StrictRedis(host="localhost", port=6379)

subscriber = client.pubsub()
subscriber.psubscribe('channel_test')

while True:
    messages = subscriber.get_message()

    if messages:
        data = messages["data"]
        
        print(data)
        
        if data == 1 or data == '1':
            continue
        data = json.loads(data)

        if not data['path'] in _pathButtons():
            print('Atalho não registrado')
            continue
        classInstance = _pathButtons()[data['path']]
        classInstance.run()