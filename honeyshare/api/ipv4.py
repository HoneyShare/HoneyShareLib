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

    def list(
        self,
        pagenum: int = None,
        pagesize: int = None,
        range: str = None,
        metadata: bool = False,
    ):
        return self.get(
            "/ipv4",
            pagenum=pagenum,
            pagesize=pagesize,
            range=range,
            metadata=metadata,
        )

    @ensureAttr("_ipv4", ExIPv4IPNeeded)
    def ipv4(self, metadata: bool = False):
        return self.get(f"/ipv4/{self._ipv4}", metadata=metadata)

    @ensureAttr("_ipv4", ExIPv4IPNeeded)
    def ports(
        self,
        pagenum: int = None,
        pagesize: int = None,
        metadata: bool = False,
    ):
        return self.get(
            f"/ipv4/{self._ipv4}/ports",
            pagenum=pagenum,
            pagesize=pagesize,
            metadata=metadata,
        )

    @ensureAttr("_ipv4", ExIPv4IPNeeded)
    def hostnames(
        self,
        pagenum: int = None,
        pagesize: int = None,
        metadata: bool = False,
    ):
        return self.get(
            f"/ipv4/{self._ipv4}/hostnames",
            pagenum=pagenum,
            pagesize=pagesize,
            metadata=metadata,
        )

    @ensureAttr("_ipv4", ExIPv4IPNeeded)
    def timeseries(
        self,
        pagenum: int = None,
        pagesize: int = None,
        has_volume: bool = None,
        has_pcap: bool = None,
        port: str = None,
        metadata: bool = False,
    ):
        if port is None:
            return self.get(
                f"/ipv4/{self._ipv4}/timeseries",
                pagenum=pagenum,
                pagesize=pagesize,
                has_volume=has_volume,
                has_pcap=has_pcap,
                metadata=metadata,
            )
        return self.get(
            f"/ipv4/{self._ipv4}/ports/{port}/timeseries",
            pagenum=pagenum,
            pagesize=pagesize,
            has_volume=has_volume,
            has_pcap=has_pcap,
            metadata=metadata,
        )

    @ensureAttr("_ipv4", ExIPv4IPNeeded)
    def payload(
        self,
        port: str,
        pagenum: int = None,
        pagesize: int = None,
        metadata: bool = False,
        base64_decode: bool = False,
    ):
        res = self.get(
            f"/ipv4/{self._ipv4}/ports/{port}/payload",
            pagenum=pagenum,
            pagesize=pagesize,
            metadata=metadata,
        )

        if base64_decode:
            for i in res["Connections"]:
                i["Payload"] = bytes_functions.base64_decode(i["Payload"])

        return res
