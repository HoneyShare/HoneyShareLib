from abc import ABC

from honeyshare import config, api


class HoneyShare:
    def __init__(self, key=None):
        self.key = key or config.KEY
        self.Blacklist = api.Blacklist(self.key)
        self.IPv4 = api.IPv4(self.key)
        self.Hostnames = api.Hostnames(self.key)
        self.Ports = api.Ports(self.key)
