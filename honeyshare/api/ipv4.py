from honeyshare.api.api_common import APICommon


class IPv4(APICommon):
    def __call__(self, ipv4: str = None):
        if ipv4 is None:
            return self.get_request("/ipv4")
        return self.get_request(f"/ipv4/{ipv4}")

    def ports(self, ipv4: str):
        return self.get_request(f"/ipv4/{ipv4}/ports")

    def bytes(self, ipv4: str, port: str):
        return self.get_request(f"/ipv4/{ipv4}/ports/{port}/bytes")
