# using python 2.7.x
# tastekid api reference https://www.tastekid.com/read/api
# configparse ref https://wiki.python.org/moin/ConfigParserExamples

from urllib2 import urlopen
from json import load 
import pprint 
import ConfigParser

#read config file
config = ConfigParser.RawConfigParser()
config.read('example.cfg')
def ConfigSectionMap(section):
    dict1 = {}
    options = config.options(section)
    for option in options:
        try:
            dict1[option] = config.get(section, option)
            if dict1[option] == -1:
                DebugPrint("skip: %s" % option)
        except:
            print("exception on %s!" % option)
            dict1[option] = None
    return dict1
# config.sections()

url = 'https://www.tastekid.com/api/similar?q='
query = raw_input('What similar movies are you looking for?').replace(" ","+")
# print query
url = url +query
# load apikey
key = ConfigSectionMap("SectionOne")['key'] 
url = url +'&k='+key
# print url
response = urlopen(url) # what exactly am I receiving here?
json_obj = load(response) # why do I have to load stuff here?
#
##print(json_obj)
#print response
#print json_obj

for i in json_obj['Similar']['Results']:
	print '- '+i['Name']

'''
# reference
Using this key, you can perform 150 requests per hour. Please provide a description of your product, together with some usage estimates. This allows us to increase the quota of certain applications that need it and get a better understanding of how the service is being used.

BASE ENDPOINT AND EXAMPLE

This retrieves recommendations for Red Hot Chili Peppers and Pulp Fiction:

https://www.tastekid.com/api/similar?q=red+hot+chili+peppers%2C+pulp+fiction

PARAMETERS

q: the search query; consists of a series (at least one) of bands, movies, TV shows, books, authors and/or games, separated by commas. Sometimes it is useful to specify the type of a certain resource in the query (e.g. if a movie and a book share the same title). You can do this by using the "band:", "movie:", "show:", "book:", "author:" or "game:" operators, for example: "band:underworld, movie:harry potter, book:trainspotting". Don't forget to encode this parameter.
type: query type, specifies the desired type of results. It can be one of the following: music, movies, shows, books, authors, games. If not specified, the results can have mixed types.
info: when set to 1, additional information is provided for the recommended items, like a description and a related Youtube clip (when available). Default is 0.
limit: maximum number of recommendations to retrieve. Default is 20.
k: Your API access key.
callback: add when using JSONP, to specify the callback function.
RESPONSE

The output of the API uses the JSON/JSONP format. To use JSONP, add a callback parameter.

The returned object contains, under the Similar key, the item(s) that were searched for (a list in the Info key) and the recommended items (a list in the Results key). Each item in a list has the Name and Type keys. The type can be music, movie, show, book, author or game.

When verbose=1 in the request, each item can also contains the following additional keys:

wTeaser: item description
wUrl: item Wikipedia URL
yUrl: item Youtube clip URL
yID: item Youtube clip ID
'''