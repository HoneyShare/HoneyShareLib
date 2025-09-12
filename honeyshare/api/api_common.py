import honeyshare.config
from honeyshare.api_requests import make_request


class APICommon:
    def __init__(self, key=None):
        self.key = key or config.KEY

    def _get(self, path, metadata=False, **params):
        resp = make_request(path, self.key, **params)

        if resp.status_code == 403:
            raise ExNotAuthenticated
        elif resp.status_code == 404:
            raise ExNotFound(path)
        elif resp.status_code != 200:
            raise ExUnknownError(resp.status_code)

        return resp

    def get(self, path, metadata=False, **params):
        resp = self._get(path, metadata=metadata, **params)

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

            if "pagesize" in js:
                self.pagesize = js["PageSize"]

            if "pagenum" in js:
                self.pagenum = js["PageNum"]
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
