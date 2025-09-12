from honeyshare.api.api_common import APICommon
from honeyshare.api.util import ensureAttr
from honeyshare import bytes_functions


class ExPortNeeded(Exception):
    def __init__(self):
        super().__init__("Port needed for operation")


class Port(APICommon):
    def __call__(
        self,
        port: str = None,
        pagenum: int = None,
        pagesize: int = None,
        metadata: bool = False,
    ):
        self._port = port
        return self

    def list(self, pagenum: int = None, pagesize: int = None, metadata: bool = False):
        return self.get("/ports", pagenum, pagesize, metadata)

    @ensureAttr("_port", ExPortNeeded)
    def port(self, metadata: bool = False):
        return self.get(f"/ports/{self._port}", metadata=metadata)

    @ensureAttr("_port", ExPortNeeded)
    def ipv4(
        self,
        ipv4: str = None,
        pagenum: int = None,
        pagesize: int = None,
        metadata: bool = False,
    ):
        if ipv4 is None:
            return self.get(
                f"/ports/{self._port}/ipv4", pagenum, pagesize, metadata=metadata
            )
        return self.get(f"/ports/{self._port}/ipv4/{ipv4}", metadata=metadata)

    @ensureAttr("_port", ExPortNeeded)
    def payload(
        self,
        ipv4: str,
        pagenum: int = None,
        pagesize: int = None,
        metadata: bool = False,
        base64_decode: bool = False,
    ):
        res = self.get(
            f"/ports/{self._port}/ipv4/{ipv4}/payload",
            pagenum,
            pagesize,
            metadata=metadata,
        )

        if base64_decode:
            for i in res["Connections"]:
                i["Payload"] = bytes_functions.base64_decode(i["Payload"])

        return res
