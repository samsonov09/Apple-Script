import webbrowser
import time

chrome = 'open -a /Applications/Google\ Chrome.app %s'

while True:
        print "Working hard to reproduce it..."
        with open("urls.txt") as f:
                for url in f:
                        webbrowser.get(chrome).open_new_tab(url.strip())
                        time.sleep(1)
