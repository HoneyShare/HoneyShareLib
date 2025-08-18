from honeyshare.api.api_common import APICommon
from honeyshare.api.util import ensureAttr


class ExTimeseriesIDNeeded(Exception):
    def __init__(self):
        super().__init__("Timeseries ID needed for operation")


class Timeseries(APICommon):
    def __call__(self, id: int = None):
        self._id = id
        return self

    def list(self, page_num: int = None, page_size: int = None, metadata: bool = False):
        return self.get(
            "/timeseries", page_num=page_num, page_size=page_size, metadata=metadata
        )

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
