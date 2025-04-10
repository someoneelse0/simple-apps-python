#!/usr/bin/python3
# -*- coding:utf-8 -*-

from PIL import Image
import tkinter as tk
from tkinter import filedialog, messagebox
import os
import smtplib
import qrcode

def send_email(host, port, from_addr, to_addr, message):
    try:
        port = int(port)
        with smtplib.SMTP(host=host, port=port) as smtp:
            smtp.sendmail(from_addr=from_addr, to_addrs=to_addr, msg=message)
        messagebox.showinfo("Success", "Email sent successfully.")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to send email:\n{e}")

def compress_image():
    file_path = filedialog.askopenfilename(title="Choose a file", filetypes=(("Images", "*.jpg *.jpeg *.png"),))
    if not file_path:
        return

    try:
        base, ext = os.path.splitext(file_path)
        if ext.lower() not in [".jpg", ".jpeg", ".png"]:
            raise ValueError("Unsupported file type.")
        
        img = Image.open(file_path)
        new_path = "compr_" + os.path.basename(file_path)
        img.save(new_path, optimize=True, quality=80)
        messagebox.showinfo("Image Saved", f"Compressed image saved as {new_path}")
    except Exception as e:
        messagebox.showerror("Image Error", f"Could not compress image:\n{e}")

def generate_qr(version, box_size, border, color, data, filename):
    try:
        version = int(version)
        box_size = int(box_size)
        border = int(border)
        if not data or not filename:
            raise ValueError("Data and filename are required.")

        qr = qrcode.QRCode(version=version, box_size=box_size, border=border)
        qr.add_data(data)
        img = qr.make_image(fill_color=color, back_color="white")
        img.save(filename + ".png")
        messagebox.showinfo("QR Code Saved", f"QR Code saved as {filename}.png")
    except Exception as e:
        messagebox.showerror("QR Error", f"Could not generate QR code:\n{e}")

def app():
    root = tk.Tk()
    root.title("SMTP, Image & QR Tool")

    vars = [tk.StringVar() for _ in range(11)]

    labels = [
        "SMTP host (e.g smtp.gmail.com):",
        "Port:",
        "From email:",
        "To email:",
        "Message:",
        "QR code version:",
        "Box size:",
        "Border size:",
        "QR color (e.g black):",
        "QR data:",
        "Output filename:"
    ]

    for i, text in enumerate(labels):
        tk.Label(root, text=text).grid(row=i, column=0, sticky="e", padx=5, pady=5)
        tk.Entry(root, textvariable=vars[i]).grid(row=i, column=1, padx=5, pady=5)

    tk.Button(root, text="Send Email", command=lambda: send_email(vars[0].get(), vars[1].get(), vars[2].get(), vars[3].get(), vars[4].get())).grid(row=5, column=2, padx=5, pady=5)

    tk.Button(root, text="Compress Image", command=compress_image).grid(row=6, column=2, padx=5, pady=10)

    tk.Button(root, text="Generate QR Code", command=lambda: generate_qr(
        vars[5].get(), vars[6].get(), vars[7].get(), vars[8].get(), vars[9].get(), vars[10].get()
    )).grid(row=13, column=0, columnspan=3, pady=10)

    root.mainloop()

if __name__ == "__main__":
    app()
