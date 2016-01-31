# python 3.4.0
# example of authenticated API request to Github using python

# resources https://stackoverflow.com/questions/17301938/making-a-request-to-a-restful-api-using-python, http://www.python-requests.org/en/latest/

import requests
import json

# url info

url = "https://api.github.com/user/issues"
headers = {'Accept': 'application/vnd.github.v3+json'}

# we could do
# r = requests.get('https://api.github.com/user', auth=('user', 'pass'))
# BUT it is a good practice not to hardcode the credentials. So ask the user to enter credentials at runtime

r = requests.get(url, headers=headers, auth=(input("username: "), input("Password: ")), verify=True)

print(r.status_code, r.headers['content-type'],r.encoding) # you can comment this out

# For successful API call, response code will be 200 (OK)
if(r.ok):

    # Loading the response data into a dict variable
    # json.loads takes in only binary or string variables so using content to fetch binary content
    # Loads (Load String) takes a Json file and converts into python data structure (dict or list, depending on JSON)
    print(r.json())
else:
  # If response code is not ok (200), print the resulting http error code with description
    r.raise_for_status()

