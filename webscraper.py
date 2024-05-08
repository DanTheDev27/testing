import requests
import urllib
import json
import os.path



request_url = requests.get('https://microsoftedge.github.io/Demos/json-dummy-data/64KB-min.json')
#data = request_url.json()

#pathtofile
path = "C:/Users/Danny/Documents/SDevSpring24/WorkStudyProjects"
fileLocation = os.path.join(path,'testFile'+'.json')
""" with open(fileLocation,'w') as file:
    json.dump(data,file) """
params = 'name'
with open(fileLocation,'r') as file:
    data= json.load(file)
formattedData= json.dumps(data[0], indent=4)
print(formattedData)



