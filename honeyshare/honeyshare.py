from abc import ABC

from honeyshare import config, api


class HoneyShare:
    def __init__(self, key=None):
        self.key = key or config.KEY
        self.Blacklist = api.Blacklist(self.key)
        self.IPv4 = api.IPv4(self.key)
        self.Hostname = api.Hostname(self.key)
        self.Port = api.Port(self.key)
        self.Timeseries = api.Timeseries(self.key)
