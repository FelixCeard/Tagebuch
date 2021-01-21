# Tagebuch
### General
The purpose of this repo is to make a diary that opens a word document every day at the same time that has no internet connection, thus, is relatively private.
The choice of Microsoft Word (Libre office or any other app) is made on purpuse, as it is easy to write in it.

### Download
Clone the repository with ```git clone https://github.com/FelixCeard/Tagebuch.git``` and run install.py. This will create a file called ```Tagebuch.bat``` that can be opened manualy every time or be placed in the startup folder to start the script every boot.
To do this, press the keys win+r and write ```shell:startup```. This will open a folder in which you can paste the ```Tagebuch.bat``` file in order to start it on every boot. Restart your PC and your word document is beeing openend every day.

### Config
To configure the time to log the diary, open the file ```config.json``` and replace the ```time``` value with the wanted hour
