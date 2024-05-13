import requests
import urllib
import json
import os.path
import csv

#url to scrape from
request_url = requests.get('https://microsoftedge.github.io/Demos/json-dummy-data/64KB-min.json')

with urllib.request.urlopen('https://microsoftedge.github.io/Demos/json-dummy-data/64KB-min.json') as url:
    data = json.load(url)
    #print(data)

for item in data:
    names = item['name']
    id = item['id']
    language = item['language']
    print(f"Full name: {names} \n Id: {id} \n {language}")







#code to save and write file

#Path where the file will be saved
path = ""
#write data to file in designated location
""" fileLocation = os.path.join(path,'testFile'+'.json')
with open(fileLocation,'w') as file:
    json.dump(data,file) """

#opening and parsing data by parameters
""" file = open(fileLocation)
jsonLoad = json.load(file)
formattedFile = json.dumps(jsonLoad, indent=4)
#print(formattedFile)
for item in jsonLoad:
    names = item['name']
    id = item['id']
    nameId = "Full name: " + names + "\n id: " + id
    print(nameId) """
