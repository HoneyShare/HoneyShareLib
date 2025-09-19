import pytest
from unittest.mock import patch, ANY

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


@patch("honeyshare.api_requests.requests")
class TestMakeRequest:
    key = "key"

    params = [
        {},
        {"a": 10},
        {"b": 20},
        {"a": 10, "b": 20},
    ]

    @pytest.mark.parametrize("path", PathsPositive)
    def test_positive_make_request_without_params(self, requests_mock, path):
        resp = api_requests.make_request(path, self.key)
        requests_mock.get.assert_called_once_with(
            ANY,
            headers={config.HEADER: self.key},
            params={},
        )

    @pytest.mark.parametrize("path", PathsPositive)
    @pytest.mark.parametrize("params", params)
    def test_positive_make_request_with_params(self, requests_mock, path, params):
        resp = api_requests.make_request(path, self.key, **params)
        requests_mock.get.assert_called_once_with(
            ANY,
            headers={config.HEADER: self.key},
            params=params,
        )

    @pytest.mark.parametrize("path", PathsNegative)
    def test_negative_make_request_without_params(self, requests_mock, path):
        with pytest.raises(api_requests.ExInvalidPath):
            api_requests.make_request(path, self.key)

    @pytest.mark.parametrize("path", PathsNegative)
    @pytest.mark.parametrize("params", params)
    def test_negative_make_request_with_params(self, requests_mock, path, params):
        with pytest.raises(api_requests.ExInvalidPath):
            api_requests.make_request(path, self.key, **params)
