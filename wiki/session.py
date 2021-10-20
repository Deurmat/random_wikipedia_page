import requests
import logging


class WikiRandomizer():
    def __init__(self):
        self.url = "https://en.wikipedia.org/w/api.php"
        self.params = {
            "action": "query",
            "format": "json",
            # "list": "random",
            "generator": "random",
            "grnlimit": "1",
            "grnnamespace": 0,
            "prop": "info",
            "inprop": "url"
        }
        self.logger = logging.getLogger("__name__")

        self.session = requests.Session()

    def get_random_page(self):
        self.request = self.session.get(url=self.url, params=self.params)
        self.request_json = self.request.json()
        # print(j['query']['random'])

        # print(self.request_json)
        id = list(self.request_json['query']['pages'])[0]
        url = self.request_json['query']['pages'][id]['fullurl']
        print(f'Your URL is {url}')

        return url

# http://it.wikipedia.org/w/api.php?action=query&list=search&srsearch=calvino&format=xml&srprop=snippet

# http://it.wikipedia.org/w/api.php?action=query&generator=search&gsrsearch=calvino&format=xml&gsrprop=snippet&prop=info&inprop=url
