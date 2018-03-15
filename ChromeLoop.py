import subprocess
import webbrowser
from time import sleep
import os

open_chromes = [
                'https://yahoo.com',
                'https://dlptest.com/',
                'https://www.youtube.com/',]
for chrome in open_chromes:
    cmd = ['open', '-na', 'Google Chrome']
    cmd.append(chrome)
    subprocess.call(cmd)

sleep(3)

chrome = 'open -a /Applications/Google\ Chrome.app %s'
a=0

while True:
    webbrowser.get(chrome).open_new("http://yahoo.com")
    webbrowser.get(chrome).open_new("https://dlptest.com")
    sleep(8)
