import honeyshare.config
from honeyshare.api_requests import make_request


class APICommon:
    def __init__(self, key=None):
        self.key = key or config.KEY

    def get_request(self, path, page_num=None, page_size=None):
        req = make_request(path, self.key, page_num, page_size)

        if req.status_code == 403:
            raise ExNotAuthenticated
        elif req.status_code != 200:
            raise ExUnknownError

        try:
            return req.json()
        except:
            raise ExCannotParseJSON


class ExNotAuthenticated(Exception):
    def __init__(self):
        super().__init__("Not authenticated")


class ExUnknownError(Exception):
    def __init__(self):
        super().__init__("Unknown Error")


class ExCannotParseJSON(Exception):
    def __init__(self):
        super().__init__("Cannot Parse JSON")
