import json
import csv
import os.path
import time

if __name__ == '__main__':

    with open('input.csv', 'r') as f:
        reader = csv.reader(f)
        data = list(reader)

    messages = []
    for row in data:
        messages.append({'time': float(row[0]), 'data': row[1]})

    out = []
    tLast = messages[0]["time"]
    for message in messages:
        out.append({'dt': message['time'] - tLast, 'data': message['data']})
        tLast = message['time']

    if not os.path.exists('output'):
        os.makedirs('output')
    with open(f'output/websocketData_{time.time()}.json', 'w') as f:
        json.dump(out, f, indent=2)
