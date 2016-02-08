from urllib.request import urlopen
from urllib.error  import URLError


url = 'http://placekitten.com/'

try:
	response = urlopen(url)
	# response = urllib.request.urlopen(request)
	print(response.read().decode('utf-8')[559:1000])
except URLError as e: 
	print('you messed up son!\n',e);