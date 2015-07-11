import urllib2, json, pprint

class Client:
    def get_json(self):
        url = "http://localhost:9292"
        json_dict = json.load(urllib2.urlopen(url))
        return json_dict


if __name__ == "__main__":
    client = Client()
    json_dict = client.get_json()
    pprint.pprint(json_dict)
