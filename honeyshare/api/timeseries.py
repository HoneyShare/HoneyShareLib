from honeyshare.api.api_common import APICommon


class Timeseries(APICommon):
    def list(self, page_num: int = None, page_size: int = None, metadata: bool = False):
        return self.get_request(
            "/timeseries", page_num=page_num, page_size=page_size, metadata=metadata
        )
