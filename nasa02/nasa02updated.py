#!/usr/bin/env python3
import requests
##Define NEOapi
def main():
    neourl = 'https://api.nasa.gov/neo/rest/v1/feed?'
    sd=input('Whats the startdate')
    ED=input('whats the enddate')
    startdate = 'sd()'
    enddate = '&ED()'
    mykey = '&api_key=lr1tZ19IhR5SOuMbzBxtRkz9a2zXCaTNtAxtffE7'

    neourl = neourl + startdate + mykey
    neojson = (requests.get(neourl)).json()
    print(neojson)
main()
