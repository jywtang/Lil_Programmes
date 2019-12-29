import json
import urllib.request, urllib.parse, urllib.error
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter URL: ")


print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx)
doc = uh.read().decode()
info = json.loads(doc)

total = 0
for n in info["comments"]:
    total += n["count"]
print(total)
