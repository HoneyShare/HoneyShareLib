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
            js = req.json()
        except:
            raise ExCannotParseJSON

        return APIResponse(js)


class APIResponse:
    def __init__(self, js):
        self.endpoint = js["Endpoint"]
        self.result = js["Result"]

        if "page_size" in js:
            self.page_size = js["PageSize"]

        if "page_num" in js:
            self.page_num = js["PageNum"]


class ExNotAuthenticated(Exception):
    def __init__(self):
        super().__init__("Not authenticated")


class ExUnknownError(Exception):
    def __init__(self):
        super().__init__("Unknown Error")


class ExCannotParseJSON(Exception):
    def __init__(self):
        super().__init__("Cannot Parse JSON")
