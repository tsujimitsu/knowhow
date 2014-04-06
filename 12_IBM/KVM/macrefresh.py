#!/usr/bin/python
#
#   macrefresh.py : Update MAC Table with broadcast ARP
#
#   2011/01/23 ver1.0
#

import socket
import fcntl
import sys
import os
import time

#--------------------------#
IfaceList = [ "eth0" ]
Interval = 30
#--------------------------#

def ifconfig(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        result = fcntl.ioctl(s.fileno(), 0x8915, (ifname+'\0'*32)[:32])
    except IOError:
        return None
    return socket.inet_ntoa(result[20:24])

if __name__ == '__main__':
    ipaddr = {}
    for iface in IfaceList:
        ipaddr[ iface ]= ifconfig( iface )

    while( 1 ):
        for iface in IfaceList:
            os.system( "arping -c 1 -I " + iface + " " + ipaddr[ iface ] + ">/dev/null 2>&1" )
        time.sleep( Interval )


