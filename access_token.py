import urllib
import sys
import urllib2
import ssl

host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=uqj3uCRooD5Ii4GRnqDp9bdm&client_secret=5XPKuyGorGyaCzkKbAr73eEKClzkFEE0'
request = urllib2.Request(host)
request.add_header('Content-Type', 'application/json; charset=UTF-8')
response = urllib2.urlopen(request)
content = response.read()
if (content):
    print(content)