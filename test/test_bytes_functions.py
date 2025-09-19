import pytest

from honeyshare import bytes_functions


class TestBase64Decode:
    positive = [
        ("", ""),
        ("SG9uZXlTaGFyZQ==", "HoneyShare"),
    ]

    negative = [
        "AAAAAA",
        "This is not base64",
    ]

    @pytest.mark.parametrize("arg, exp", positive)
    def test_positive_base64_decode(self, arg, exp):
        act = bytes_functions.base64_decode(arg)
        assert exp == act

    @pytest.mark.parametrize("arg", negative)
    def test_negative_base64_decode(self, arg):
        act = bytes_functions.base64_decode(arg)
        assert arg == act
