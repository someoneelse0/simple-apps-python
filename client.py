#!/bin/python3
# -*- coding:utf-8 -*-

import codecs, socket, nacl.utils
from nacl.public import PrivateKey, PublicKey, Box, SealedBox

HOST = "127.0.0.1"
PORT = 12345

def process_message(sock, box, sb, sbp, nonce):
    try:
        message = input("Introduce your message: ")
        encoded = codecs.encode(message[::-1], encoding="rot_13")
        encrypted = box.encrypt(encoded.encode(), nonce)
        final_encrypted = sb.encrypt(encrypted)
        sock.send(final_encrypted)

        response = sock.recv(4096)
        decrypted_sealed = sbp.decrypt(response)
        plain_bytes = box.decrypt(decrypted_sealed)
        print("rot13 server:", plain_bytes)
        decoded = codecs.encode(plain_bytes.decode()[::-1], encoding="rot_13")
        print("message server:", decoded)
    except Exception as e:
        print(f"[!] Error: {e}")

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((HOST, PORT))
        print(f"[+] Connected to {HOST}:{PORT}")

        nonce = nacl.utils.random(Box.NONCE_SIZE)

        server_pubkey_data = sock.recv(32)
        private_key = PrivateKey.generate()
        public_key = private_key.public_key
        sock.send(public_key.encode())

        server_pubkey = PublicKey(server_pubkey_data)

        box = Box(private_key, server_pubkey)
        sb = SealedBox(server_pubkey)
        sbp = SealedBox(private_key)

        for _ in range(10):
            process_message(sock, box, sb, sbp, nonce)
if __name__ == "__main__":
    main()
