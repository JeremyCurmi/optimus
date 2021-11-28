import json
import requests


def get_encouraging_quote() -> str:
    url = "https://zenquotes.io/api/random"
    response = json.loads(requests.get(url=url).text)
    quote = response[0]['q']
    author = response[0]['a']
    return quote + ' - ' + author
