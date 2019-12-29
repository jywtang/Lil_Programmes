import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Ask for user inputs
url = input('Enter - ')
pos = int(input("Position: "))
num= int(input("Number of times: "))

#parse html from web
for times in range(num):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    # Retrieve all of the anchor tags
    tags = soup('a')
    print(tags[pos-1].get('href', None),tags[pos-1].contents[0])
    url = tags[pos-1].get('href', None)
