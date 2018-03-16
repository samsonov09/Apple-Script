import webbrowser
  
chrome = 'open -a /Applications/Google\ Chrome.app %s'

with open("urls.txt") as f:
    for url in f:
        webbrowser.get(chrome).open_new_tab(url.strip())
