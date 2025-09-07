# HoneyShareLib

The [HoneyShare](https://honeyshare.live/) API Client.

## Installing

Available in [PYPI](https://pypi.org/project/honeyshare/).

    pip install honeyshare

## Usage

Initialize HoneyShare with a [Key](https://honeyshare.live/licenses):

    from honeyshare import HoneyShare

    hs = HoneyShare(key="Your HoneyShare Key"")

The library is organized around the five HoneyShare objects:

    hs.Blacklist.ipv4s()     // Blacklists of IPs
    hs.Blacklist.hostnames() // Blacklists of Hostnames

    hs.IPv4.list()               // IP list
    hs.IPv4(ip).ipv4()           // IP's meta data
    hs.IPv4(ip).ports()          // Ports accessed by IP
    hs.IPv4(ip).hostnames()      // Hostnames of IP
    hs.IPv4(ip).timeseries()     // Timeseries of IP
    hs.IPv4(ip).timeseries(port) // Timeseries of IP on Port
    hs.IPv4(ip).payload(port)    // Payload sent by IP on Port

    hs.Hostname.list()               // Hostname list
    hs.Hostname(hostname).hostname() // Hostname's meta data
    hs.Hostname(hostname).ipv4()     // IPs of Hostname

    hs.Port.list()            // List of Ports
    hs.Port(port).port()      // Port's meta data
    hs.Port(port).ipv4()      // IP's that acceed port
    hs.Port(port).ipv4(ip)    // IP's meta data on Port
    hs.Port(port).payload(ip) // Payload sent by IP on Port

    hs.Timeseries.list() // List all connections

## Building and Installing Locally

    poetry build
    pip install --force-reinstall dist/honeyshare-*.whl
