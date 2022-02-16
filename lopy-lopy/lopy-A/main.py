#!/usr/bin/env python
#
# Copyright (c) 2019, Pycom Limited.
#
# This software is licensed under the GNU GPL version 3 or any
# later version, with permitted additional terms. For more information
# see the Pycom Licence v1.0 document supplied with this file, or
# available at https://www.pycom.io/opensource/licensing
#

from network import LoRa
import socket
import time

lora = LoRa(mode=LoRa.LORA,region=LoRa.US915, frequency=915000000)
s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
s.setblocking(False)
print('Start')

i=0
while True:
    if s.recv(64) == b'Ping':
        print('Ping Recived')
        s.send('Pong'+ i)
        i+1
    time.sleep(5)
