#!/usr/bin/env python3
import urllib.request
import json
import webbrowser

apodurl = 'https://api.nasa.gov/planetary/apod?'
mykey = 'api_key=lr1tZ19IhR5SOuMbzBxtRkz9a2zXCaTNtAxtffE7'

apodurlobj = urllib.request.urlopen(apodurl + mykey)

apodread = apodurlobj.read()

decodeapod = json.loads(apodread.decode('utf-8'))

print("\n\nConverted puthon data")
print(decodeapod)

input('\nPress Enter to open NASA Picture of the Day in Firefox')
webbrowser.open(decodeapod['url'])

