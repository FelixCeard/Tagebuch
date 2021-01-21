import os

dirname = os.getcwd().replace('\\', '/')
print(dirname)
bach = f"py {dirname}/main.py"
bach = f"@echo off\nstart /B py {dirname}/main.py &"
with open('Tagebuch.bat', 'w') as file:
    file.write(bach)
