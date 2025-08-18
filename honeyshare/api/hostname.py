from honeyshare.api.api_common import APICommon
from honeyshare.api.util import ensureAttr


class ExHostnameNeeded(Exception):
    def __init__(self):
        super().__init__("Hostname needed for operation")


class Hostname(APICommon):
    def __call__(self, hostname: str = None):
        self._hostname = hostname
        return self

    @ensureAttr("_hostname", ExHostnameNeeded)
    def hostname(self, metadata: bool = False):
        return self.get(f"/hostnames/{self._hostname}", metadata=metadata)

    def list(self, page_num: int = None, page_size: int = None, metadata: bool = False):
        return self.get(
            "/hostnames", page_num=page_num, page_size=page_size, metadata=metadata
        )

    @ensureAttr("_hostname", ExHostnameNeeded)
    def ipv4(
        self,
        page_num: int = None,
        page_size: int = None,
        metadata: bool = False,
    ):
        return self.get(
            f"/hostnames/{self._hostname}/ipv4",
            page_num=page_num,
            page_size=page_size,
            metadata=metadata,
        )
