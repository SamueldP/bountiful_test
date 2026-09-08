import urllib.request
import json

url = "https://bountiful-test.blogspot.com/feeds/posts/default/157488570619266794?alt=json"
req = urllib.request.Request(url)
with urllib.request.urlopen(req) as response:
    data = json.loads(response.read().decode())
    print(data['entry']['title']['$t'])
