# using python 2.7.x
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

url = 'http://api.npr.org/query?apiKey='
key = ConfigSectionMap("SectionOne")['key'] 

url = url +key
url += '&numResults=3&format=json&id='
url += raw_input('Which NPR ID do you want to query?')

response = urlopen(url) # what exactly am I receiving here?
json_obj = load(response) # why do I have to load stuff here?

# pprint.pprint(json_obj)

for story in json_obj['list']['story']:
	print(story['title']['$text'])