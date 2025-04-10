#!/bin/python3
# -*- coding:utf-8 -*-

import codecs, socket, nacl.utils
from nacl.public import PrivateKey, PublicKey, Box, SealedBox

HOST = "127.0.0.1"
PORT = 12345

def process_message(conn, box, sb, sbp, nonce):
    try:
        encrypted = conn.recv(4096)
        decrypted_sealed = sb.decrypt(encrypted)
        plain_bytes = box.decrypt(decrypted_sealed)

        decoded = plain_bytes.decode()
        print("rot13 client:", decoded.encode())
        message = codecs.encode(decoded[::-1], encoding="rot_13")
        print("message client:", message)

        reply = input("Introduce your message: ")
        reply_encoded = codecs.encode(reply[::-1], encoding="rot_13")
        reply_encrypted = box.encrypt(reply_encoded.encode(), nonce)
        final_encrypted = sbp.encrypt(reply_encrypted)
        conn.send(final_encrypted)
    except Exception as e:
        print(f"[!] Error: {e}")

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((HOST, PORT))
        server_socket.listen(1)
        print(f"[+] Server listening on {HOST}:{PORT}")

        while True:
            conn, addr = server_socket.accept()
            with conn:
                print(f"[+] Connection from {addr}")
                
                nonce = nacl.utils.random(Box.NONCE_SIZE)

                private_key = PrivateKey.generate()
                public_key = private_key.public_key
                conn.send(public_key.encode())

                client_pubkey_data = conn.recv(32)
                client_pubkey = PublicKey(client_pubkey_data)
                box = Box(private_key, client_pubkey)
                sb = SealedBox(private_key)
                sbp = SealedBox(client_pubkey)

                # Conversation loop
                for _ in range(10):
                    process_message(conn, box, sb, sbp, nonce)

if __name__ == "__main__":
    main()
