import json
from urllib.error import HTTPError
from urllib.parse import urlencode
from urllib.request import Request, urlopen

from honeyshare import config


def make_url(path):
    if path is None or path == "" or path[0] != "/":
        raise ExInvalidPath(path)
    return f"https://{config.HOSTNAME}/{config.API_BASE}{path}"


def make_request(path, key, **params):
    url = make_url(path)
    if params:
        url = f"{url}?{urlencode(params)}"

    request = Request(url, headers={config.HEADER: key})

    try:
        raw = urlopen(request)
    except HTTPError as e:
        raw = e

    return Response(raw)


class Response:
    def __init__(self, raw):
        self._raw = raw
        self._content = None
        self.status_code = getattr(raw, "status", None)
        if self.status_code is None:
            self.status_code = getattr(raw, "code", None)

    def _read(self):
        if self._content is None:
            self._content = self._raw.read()
        return self._content

    def json(self):
        return json.loads(self._read())

    def iter_content(self, chunk_size=8192):
        if self._content is not None:
            for i in range(0, len(self._content), chunk_size):
                yield self._content[i : i + chunk_size]
            return

        while True:
            chunk = self._raw.read(chunk_size)
            if not chunk:
                break
            yield chunk


class ExInvalidPath(Exception):
    def __init__(self, path):
        super().__init__(f"Invalid path: {path}")
