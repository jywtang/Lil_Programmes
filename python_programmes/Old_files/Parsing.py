import re, urllib.request, urllib.parse

url='https://pythonprogramming.net/'
values={'s':'basic',
        'submit':'search'}

data = urllib.parse.urlencode(values)
data = data.encode('utf-8')
req = urllib.request.Request(url, data)
resp = urllib.request.urlopen(req)
respData = resp.read()

paragraphs = re.findall(r'<p>(.*?)</p>',str(respData))

for eachPara in paragraphs:
    print(eachPara, end = '\n\n')
