#!/usr/bin/python3

# revised by Jack Christensen

import socket

addr_info = socket.getaddrinfo("towel.blinkenlights.nl", 23)
for addr in addr_info:
    if len(addr[-1]) == 2:  # look for an ipv4 address
        break
s = socket.socket()
s.connect(addr[-1])

while True:
    data = s.recv(500)
    print(str(data, 'utf8'), end='')
    
