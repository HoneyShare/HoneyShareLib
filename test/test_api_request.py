import pytest
from unittest.mock import patch
from urllib.error import HTTPError
from urllib.parse import urlencode

from honeyshare import api_requests, config


PathsPositive = [
    "/",
    "/path",
    "/path/to/resource",
    "/path/to/resource/",
]

PathsNegative = [
    None,
    "",
    "path",
    "path/to/resource",
    "path/to/resource/",
]


class TestMakeUrl:
    @pytest.mark.parametrize("arg", PathsPositive)
    def test_positive_make_url(self, arg):
        url = api_requests.make_url(arg)
        assert url.endswith(url)
        assert url.startswith("https://")
        assert config.HOSTNAME in url
        assert config.API_BASE in url

    @pytest.mark.parametrize("arg", PathsNegative)
    def test_negative_make_url(self, arg):
        with pytest.raises(api_requests.ExInvalidPath):
            api_requests.make_url(arg)


@patch("honeyshare.api_requests.urlopen")
class TestMakeRequest:
    key = "key"

    params = [
        {},
        {"a": 10},
        {"b": 20},
        {"a": 10, "b": 20},
    ]

    def assert_request(self, urlopen_mock, path, params):
        request = urlopen_mock.call_args.args[0]
        expected_url = api_requests.make_url(path)
        if params:
            expected_url = f"{expected_url}?{urlencode(params)}"
        assert request.full_url == expected_url
        assert request.get_header(config.HEADER.capitalize()) == self.key

    @pytest.mark.parametrize("path", PathsPositive)
    def test_positive_make_request_without_params(self, urlopen_mock, path):
        api_requests.make_request(path, self.key)
        self.assert_request(urlopen_mock, path, {})

    @pytest.mark.parametrize("path", PathsPositive)
    @pytest.mark.parametrize("params", params)
    def test_positive_make_request_with_params(self, urlopen_mock, path, params):
        api_requests.make_request(path, self.key, **params)
        self.assert_request(urlopen_mock, path, params)

    @pytest.mark.parametrize("path", PathsNegative)
    def test_negative_make_request_without_params(self, urlopen_mock, path):
        with pytest.raises(api_requests.ExInvalidPath):
            api_requests.make_request(path, self.key)

    @pytest.mark.parametrize("path", PathsNegative)
    @pytest.mark.parametrize("params", params)
    def test_negative_make_request_with_params(self, urlopen_mock, path, params):
        with pytest.raises(api_requests.ExInvalidPath):
            api_requests.make_request(path, self.key, **params)

    def test_make_request_returns_http_error_response(self, urlopen_mock):
        urlopen_mock.side_effect = HTTPError(
            api_requests.make_url("/"), 404, "Not Found", {}, None
        )

        resp = api_requests.make_request("/", self.key)

        assert resp is not None
        assert resp.status_code == 404
