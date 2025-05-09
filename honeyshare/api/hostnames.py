from honeyshare.api.api_common import APICommon


class Hostnames(APICommon):
    def __call__(
        self, hostname: str = None, page_num: int = None, page_size: int = None
    ):
        if hostname is None:
            return self.get_request("/hostnames", page_num, page_size)
        return self.get_request(f"/hostnames/{hostname}")

    def ipv4s(self, hostname: str, page_num: int = None, page_size: int = None):
        return self.get_request(f"/hostnames/{hostname}/ipv4", page_num, page_size)
