from honeyshare.api.api_common import APICommon


class Ports(APICommon):
    def __call__(self, port: str = None, page_num: int = None, page_size: int = None):
        if port is None:
            return self.get_request("/ports", page_num, page_size)
        return self.get_request(f"/ports/{port}")

    def ipv4(self, port: str):
        return self.get_request(f"/ports/{port}/ipv4", page_num, page_size)

    def bytes(self, port: str, ipv4: str, page_num: int = None, page_size: int = None):
        return self.get_request(f"/ports/{port}/ipv4/{ipv4}/bytes", page_num, page_size)
