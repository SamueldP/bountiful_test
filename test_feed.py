import urllib.request
import json

url = "https://bountiful-test.blogspot.com/feeds/posts/default?alt=json"
req = urllib.request.Request(url)
with urllib.request.urlopen(req) as response:
    data = json.loads(response.read().decode())
    for entry in data['feed']['entry']:
        print(entry['id']['$t'])
