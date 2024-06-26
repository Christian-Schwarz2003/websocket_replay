import json
import os
import time

if __name__ == '__main__':
    with open('input.har', 'r') as f:
        data = json.load(f)
    messages = data['log']['entries'][0]["_webSocketMessages"]
    out = []
    tLast = messages[0]['time']
    for message in messages:
        if message['type'] == 'receive':
            out.append({'dt': message['time'] - tLast, 'data': message['data']})
            tLast = message['time']
    if not os.path.exists('output'):
        os.makedirs('output')
    with open(f'output/websocketData_{time.time()}.json', 'w') as f:
        json.dump(out, f, indent=2)
