import honeyshare.config
from honeyshare.api_requests import make_request


class APICommon:
    def __init__(self, key=None):
        self.key = key or config.KEY

    def _get(self, path, page_num=None, page_size=None, metadata=False):
        resp = make_request(path, self.key, page_num, page_size)

        if resp.status_code == 403:
            raise ExNotAuthenticated
        elif resp.status_code == 404:
            raise ExNotFound(path)
        elif resp.status_code != 200:
            raise ExUnknownError(resp.status_code)

        return resp

    def get(self, path, page_num=None, page_size=None, metadata=False):
        resp = self._get(
            path, page_num=page_num, page_size=page_size, metadata=metadata
        )

        try:
            js = resp.json()
        except:
            raise ExCannotParseJSON

        if metadata:
            return APIResponse(js)

        try:
            return js["Result"]
        except KeyError as e:
            raise ExResponseMalformed(e)

    def get_file(self, path, filename, metadata=False):
        resp = self._get(path, metadata=metadata)

        with open(filename, "wb") as file:
            for chunk in resp.iter_content(chunk_size=8192):
                file.write(chunk)


class APIResponse:
    def __init__(self, js):
        try:
            self.endpoint = js["Endpoint"]
            self.result = js["Result"]

            if "page_size" in js:
                self.page_size = js["PageSize"]

            if "page_num" in js:
                self.page_num = js["PageNum"]
        except KeyError as e:
            raise ExResponseMalformed(e)


class ExNotAuthenticated(Exception):
    """
    HTTP: 403
    """

    def __init__(self):
        super().__init__("Not authenticated")


class ExNotFound(Exception):
    """
    HTTP: 404
    """

    def __init__(self, path):
        super().__init__(f"Not Found: {path}")


class ExUnknownError(Exception):
    def __init__(self, code):
        super().__init__(f"Unknown Error. Code: {code}")


class ExCannotParseJSON(Exception):
    def __init__(self):
        super().__init__("Cannot Parse JSON")


class ExResponseMalformed(Exception):
    def __init__(self, key_error):
        missing = key_error.args[0]
        super().__init__(f"Response is Malformed. Missing: {missing}")
