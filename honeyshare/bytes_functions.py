import base64


def base64_decode(bytes_encoded):
    try:
        return base64.b64decode(bytes_encoded).decode("utf-8")
    except (UnicodeDecodeError, base64.binascii.Error):
        return bytes_encoded
