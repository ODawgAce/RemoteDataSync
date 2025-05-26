import requests

class DataFetcher:
    def __init__(self, url: str):
        self.url = url

    def fetch(self):
        response = requests.get(self.url)
        response.raise_for_status()
        return response.json()