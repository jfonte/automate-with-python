import requests


url = 'http://placekitten.com'

try:
	response = requests.get(url)
	print(response.text[559:1000])
except: 
	print('you messed up son!');