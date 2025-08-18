from honeyshare.api.api_common import APICommon


class Blacklist(APICommon):
    def ipv4s(self):
        return self.get("/blacklist/ipv4s")

    def hostnames(self):
        return self.get("/blacklist/hostnames")
