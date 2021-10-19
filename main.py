import requests

s = requests.Session()

url = "https://en.wikipedia.org/w/api.php"
params = {
    "action": "query",
    "format": "json",
    "list": "random",
    "rnlimit": "1"
}

r = s.get(url=url, params=params)
j = r.json()
#print(j['query']['random'])

base_url = f"https://en.wikipedia.org/?curid={j['query']['random'][0]['id']}"
print(f'Your URL is {base_url}')
