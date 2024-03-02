import json

file = '/mnt/d/git/test/jonha.json'
with open(file, 'r') as f:
    data = json.load(f)

print(f'\nData: {data}')
