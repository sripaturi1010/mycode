#!/usr/bin/env python3

import urllib.request
import json
## Trace the iss
majortom = 'http://api.open-notify.org/astros.json'
groundctrl = urllib.request.urlopen(majortom)
helmet = groundctrl.read()
helmetson = json.loads(helmet.decode('utf-8'))
print("\n\nConverted python data")
print(helmetson)
print("\n\nConverter python data")
print(helmetson)
print("\n\nPeople in Space: ", helmetson['number'])
people = helmetson['people']
#print(people)
for all in people:
    print(all['name'] + ' on the ' + all['craft'])
#print(people[1])
