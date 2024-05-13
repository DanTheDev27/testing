import requests
import urllib
import json
import os.path


#url to scrape from
request_url = requests.get('https://microsoftedge.github.io/Demos/json-dummy-data/64KB-min.json')


data = urllib.request.urlopen('https://microsoftedge.github.io/Demos/json-dummy-data/64KB-min.json')
url = json.load(data)

for item in url:
    names = item['name']
    id = item['id']
    language = item['language']
    print(f"Full name : {names} \n Id : {id} \n language : {language}")







# *****code to save and write file*****

#Path where the file will be saved
#path = ""
#write data to file in designated location
""" fileLocation = os.path.join(path,'testFile'+'.json')
with open(fileLocation,'w') as file:
    json.dump(data,file) """
