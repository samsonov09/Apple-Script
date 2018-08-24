import webbrowser
import time
import os

url = 'https://yahoo.com'
url2 = 'https://chrome.google.com/webstore/category/extensions?hl=en'
url3 = 'https://dlptest.com'

chrome = 'open -a /Applications/Google\ Chrome.app %s'

for i in range(10,3):
	print("In progress")
	time.sleep(5)
	webbrowser.get(chrome).open_new(url2)
	time.sleep(5)
	webbrowser.get(chrome).open_new(url3)
	time.sleep(8)
	os.system("killall -9 'Google Chrome'")
	print("Done")
