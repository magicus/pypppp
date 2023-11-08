"""Module providing the packet layer of the PPPP protocol."""

# This is a library that implements the P2P protocol used by several (typically
# cheap Chinese) IoT devices, such as IP cameras. The protocol has two layers,
# a basic package layer based on UDP, which creates data channels. On these
# channels commands can be sent using the command protocol, and video and audio
# can be streamed.abs

# This file contains the implementation of the basic package layer. It also
# contains the discovery mechanism, which is based on broadcasting a magic
# packet on the local network, and waiting for devices to report back.

import logging

logger = logging.getLogger(__name__)


class PpppProtocol:
    """The class representing the packet layer of the PPPP protocol."""

    def __init__(self, local_ip):
        self.local_ip = local_ip
