import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter URL: ")

print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx)
doc = uh.read().decode()
tree = ET.fromstring(doc)
lst = tree.find("comments").findall("comment")

print(sum( [int(n.find("count").text) for n in lst]))
