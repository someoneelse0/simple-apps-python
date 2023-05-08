#!/bin/python3
#-*- coding:utf8 -*-

import codecs, socket, nacl.utils
from nacl.public import PrivateKey, PublicKey, Box, SealedBox

h="127.0.0.1"
p=12345
sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.bind((h,p))
sock.listen(1)

def f():
	m=conn.recv(1024)
	enc=sb.decrypt(m)
	enc=box.decrypt(enc)
	msg=codecs.encode(enc.decode()[::-1],encoding="rot_13")
	print("rot13 client:",enc)
	print("message client:",msg)
	i=input("Introduce your message: ")
	i=codecs.encode(i[::-1],encoding="rot_13")
	i=box.encrypt(i.encode(),n)
	encc=sbp.encrypt(i)
	conn.send(encc)

while True:
	(conn,addr)=sock.accept()
	n=nacl.utils.random(Box.NONCE_SIZE)
	prk0=PrivateKey.generate()
	pbk0=prk0.public_key
	conn.send(pbk0.encode())
	pbk1=conn.recv(32)
	ppbk1=PublicKey(pbk1)
	box=Box(prk0,ppbk1)
	sb=SealedBox(prk0)
	sbp=SealedBox(ppbk1)
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
