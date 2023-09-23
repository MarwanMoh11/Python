import urllib.request, urllib.parse, urllib.error
import json
import ssl


serviceurl = 'https://py4e-data.dr-chuck.net/json?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter location: ')
    if len(address) < 1: break
    params = {'address': address}
    params['key'] = 42
    
    url = serviceurl + urllib.parse.urlencode(params)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    newdata = json.loads(data)
    print('Retrieving ', url)
    print('Retrieved', len(data), 'characters')

    print (newdata["results"][0]["place_id"])