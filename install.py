import os
import json

dirname = os.getcwd().replace('\\', '/')
print(dirname)
bach = f"@echo off\nSTART /B pythonw {dirname}/src/main.py --wd {dirname} &"
with open('Tagebuch.bat', 'w') as file:
    file.write(bach)
with open('config.json', 'r') as file:
    j = ''.join(file.readlines())
    conf = json.loads(j)
conf['cwd'] = dirname+'src'
with open('config.json', 'w') as file:
    json.dump(conf, file, indent=2)
