import requests
from pprint import pprint

base_uri: str = "https://unidata.vercel.app"

root_response = requests.get(base_uri)
pprint(root_response.json())
