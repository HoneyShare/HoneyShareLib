import honeyshare.config
from honeyshare.api_requests import make_request


class APICommon:
    def __init__(self, key=None):
        self.key = key or config.KEY

    def get_request(self, path):
        return make_request(path, self.key)
