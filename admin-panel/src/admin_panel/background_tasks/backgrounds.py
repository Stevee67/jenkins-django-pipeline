import requests
import os


class SanicDemoSource:
    url = 'http://{{host}}:8800/health-check'.format(host=os.getenv('SANIC_HOST', 'localhost'))

    def __init__(self):
        pass

    def run(self):
        return requests.get(self.url).json()
