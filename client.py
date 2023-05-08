#!/bin/python3
#-*- coding:utf8 -*-

import codecs, socket, nacl.utils
from nacl.public import PrivateKey, PublicKey, Box, SealedBox

h="127.0.0.1"
p=12345
sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.connect((h,p))

def f():
	i=input("Introduce your message: ")
	i=codecs.encode(i[::-1],encoding="rot_13")
	i=box.encrypt(i.encode(),n)
	encc=sb.encrypt(i)
	sock.send(encc)
	mm=sock.recv(1024)
	sbm=sbp.decrypt(mm)
	msg=box.decrypt(sbm)
	m=codecs.encode(msg.decode()[::-1],encoding="rot_13")
	print("rot13 server:",msg)
	print("message server:",m)

while True:
	n=nacl.utils.random(Box.NONCE_SIZE)
	prk0=PrivateKey.generate()
	pbk0=prk0.public_key
	pbk1=sock.recv(32)
	sock.send(pbk0.encode())
	ppbk1=PublicKey(pbk1)
	box=Box(prk0,ppbk1)
	sb=SealedBox(ppbk1)
	sbp=SealedBox(prk0)
	f()
	f()
	f()
	f()
	f()
	f()
	f()
	f()
	f()
	f()
