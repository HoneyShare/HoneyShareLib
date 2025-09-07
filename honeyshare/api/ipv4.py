from honeyshare.api.api_common import APICommon
from honeyshare.api.util import ensureAttr
from honeyshare import bytes_functions


class ExIPv4IPNeeded(Exception):
    def __init__(self):
        super().__init__("IPv4 needed for operation")


class IPv4(APICommon):
    def __call__(self, ipv4: str = None):
        self._ipv4 = ipv4
        return self

    def list(self, page_num: int = None, page_size: int = None, metadata: bool = False):
        return self.get("/ipv4", page_num, page_size, metadata)

    @ensureAttr("_ipv4", ExIPv4IPNeeded)
    def ipv4(self, metadata: bool = False):
        return self.get(f"/ipv4/{self._ipv4}", metadata=metadata)

    @ensureAttr("_ipv4", ExIPv4IPNeeded)
    def ports(
        self,
        page_num: int = None,
        page_size: int = None,
        metadata: bool = False,
    ):
        return self.get(
            f"/ipv4/{self._ipv4}/ports",
            page_num=page_num,
            page_size=page_size,
            metadata=metadata,
        )

    @ensureAttr("_ipv4", ExIPv4IPNeeded)
    def hostnames(
        self,
        page_num: int = None,
        page_size: int = None,
        metadata: bool = False,
    ):
        return self.get(
            f"/ipv4/{self._ipv4}/hostnames",
            page_num=page_num,
            page_size=page_size,
            metadata=metadata,
        )

    @ensureAttr("_ipv4", ExIPv4IPNeeded)
    def timeseries(
        self,
        page_num: int = None,
        page_size: int = None,
        port: str = None,
        metadata: bool = False,
    ):
        if port is None:
            return self.get(
                f"/ipv4/{self._ipv4}/timeseries",
                page_num=page_num,
                page_size=page_size,
                metadata=metadata,
            )
        return self.get(
            f"/ipv4/{self._ipv4}/ports/{port}/timeseries",
            page_num=page_num,
            page_size=page_size,
            metadata=metadata,
        )

    @ensureAttr("_ipv4", ExIPv4IPNeeded)
    def payload(
        self,
        port: str,
        page_num: int = None,
        page_size: int = None,
        metadata: bool = False,
        base64_decode: bool = False,
    ):
        res = self.get(
            f"/ipv4/{self._ipv4}/ports/{port}/payload",
            page_num=page_num,
            page_size=page_size,
            metadata=metadata,
        )

        if base64_decode:
            for i in res["Connections"]:
                i["Payload"] = bytes_functions.base64_decode(i["Payload"])

        return res
