from honeyshare.api.api_common import APICommon


class Hostnames(APICommon):
    def hostnames(self, hostname: str = None):
        if hostname is None:
            return self.get_request("/hostnames")
        return self.get_request(f"/hostnames/{hostname}")

    def ipv4s(self, hostname: str):
        return self.get_request(f"/hostnames/{hostname}/ipv4")
