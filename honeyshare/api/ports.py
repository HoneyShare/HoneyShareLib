from honeyshare.api.api_common import APICommon


class Ports(APICommon):
    def __call__(self, port: str = None):
        if port is None:
            return self.get_request("/ports")
        return self.get_request(f"/ports/{port}")

    def ipv4(self, port: str):
        return self.get_request(f"/ports/{port}/ipv4")

    def bytes(self, port: str, ipv4: str):
        return self.get_request(f"/ports/{port}/ipv4/{ipv4}/bytes")
