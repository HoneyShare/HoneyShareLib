import requests

from honeyshare import config


def make_url(path):
    return f"https://{config.HOSTNAME}/{config.API_BASE}{path}"


def make_request(path, key, page_num, page_size):
    url = make_url(path)

    params = {}
    if page_num is not None:
        params["pagenum"] = page_num
    if page_size is not None:
        params["pagesize"] = page_size

    resp = requests.get(url, headers={config.HEADER: key}, params=params)
    return resp
