import requests

from honeyshare import config


def make_url(path):
    return f"https://{config.HOSTNAME}/{config.API_BASE}{path}"


def make_request(path, key, **params):
    url = make_url(path)

    resp = requests.get(url, headers={config.HEADER: key}, params=params)
    return resp
