Scapy rssi snippet 
###################

:Date: 28 Feb 2018 
:Category: python 
:Tags: scapy, python 
:Status: published

Scapy Snippets
==============

How to get RSSI from WLAN packet
--------------------------------

.. code:: python

    from scapy.layers.dot11 import RadioTap, Dot11

    def get_rssi(packet):
        if packet.haslayer(RadioTap):
            return packet.dbm_antsignal

**caveat: currently only tested on Ralink: RT5370 chipset**
