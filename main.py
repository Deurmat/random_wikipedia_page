import requests

s = requests.Session()

url = "https://en.wikipedia.org/w/api.php"
params = {
    "action": "query",
    "format": "json",
    # "list": "random",
    "generator": "random",
    "rnlimit": "1",
    "rnnamespace": 0,
    "prop": "links"
}

r = s.get(url=url, params=params)
j = r.json()
#print(j['query']['random'])
print(j)
base_url = f"https://en.wikipedia.org/?curid={j['query']['random'][0]['id']}"
print(f'Your URL is {base_url}')

# http://it.wikipedia.org/w/api.php?action=query&list=search&srsearch=calvino&format=xml&srprop=snippet

# http://it.wikipedia.org/w/api.php?action=query&generator=search&gsrsearch=calvino&format=xml&gsrprop=snippet&prop=info&inprop=url
