from honeyshare.api.api_common import APICommon
from honeyshare.api.util import ensureAttr


class ExTimeseriesIDNeeded(Exception):
    def __init__(self):
        super().__init__("Timeseries ID needed for operation")


class Timeseries(APICommon):
    def __call__(self, id: int = None):
        self._id = id
        return self

    def list(
        self,
        pagenum: int = None,
        pagesize: int = None,
        has_volume: bool = None,
        has_pcap: bool = None,
        metadata: bool = False,
    ):
        return self.get(
            "/timeseries",
            pagenum=pagenum,
            pagesize=pagesize,
            has_volume=has_volume,
            has_pcap=has_pcap,
            metadata=metadata,
        )

    @ensureAttr("_id", ExTimeseriesIDNeeded)
    def conn(self, metadata: bool = False):
        return self.get(f"/timeseries/{self._id}", metadata=metadata)

    @ensureAttr("_id", ExTimeseriesIDNeeded)
    def volume(self, filename: str, metadata: bool = False):
        return self.get_file(
            f"/timeseries/{self._id}/volume", filename, metadata=metadata
        )

    @ensureAttr("_id", ExTimeseriesIDNeeded)
    def pcap(self, filename: str, metadata: bool = False):
        return self.get_file(
            f"/timeseries/{self._id}/pcap", filename, metadata=metadata
        )
