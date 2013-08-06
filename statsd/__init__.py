from __future__ import absolute_import
import os
import socket

from .client import StatsClient
from ._version import __version__


__all__ = ['StatsClient', 'statsd']

statsd = None

if 'STATSD_HOST' in os.environ:
    try:
        host = os.environ['STATSD_HOST']
        port = int(os.environ['STATSD_PORT'])
        prefix = os.environ.get('STATSD_PREFIX')
        statsd = StatsClient(host, port, prefix)
    except (socket.error, socket.gaierror, KeyError):
        pass
