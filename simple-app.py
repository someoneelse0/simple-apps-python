# -*- coding:utf-8 -*-
#!/usr/bin/python3
from PIL import Image
import tkinter as tk
from tkinter import filedialog
import os
import smtplib
import qrcode

t=tk.Tk()
t.title("SMTP")

s0=tk.StringVar()
s1=tk.StringVar()
s2=tk.StringVar()
s3=tk.StringVar()
s4=tk.StringVar()
s5=tk.StringVar()
s6=tk.StringVar()
s7=tk.StringVar()
s8=tk.StringVar()
s9=tk.StringVar()
s10=tk.StringVar()

def smtp(h,p,fd,ta,m):
        s=smtplib.SMTP(host=h,port=p)
        s.sendmail(from_addr=fd,to_addrs=ta,msg=m)

def img():
	fd=filedialog.askopenfilename(title="Choose a file",filetypes=(("JPG","*.jpg *.jpeg"),("PNG","*.png")))
	fi,ex=os.path.splitext(fd)
	if ex in [".jpg",".jpg",".png"]:
		i=Image.open(fi+ex)
		i.save("compr_"+fi+ex,optimize=True,quality=80)

def qr(vers,boxsize,bor,co,da,imnm):
	qrc=qrcode.QRCode(version=vers,box_size=boxsize,border=bor)
	qrc.add_data(da)
	i=qrc.make_image(fill_color=co,back_color="#FFFFFF")
	i.save(imnm+".png")

l0=tk.Label(t,text="SMTP Host (example smtp.gmail.com):")
l0.grid(row=0,column=0)
e0=tk.Entry(t,textvariable=s0)
e0.grid(row=0,column=1)
l1=tk.Label(t,text="Port:")
l1.grid(row=1,column=0)
e2=tk.Entry(t,textvariable=s1)
e2.grid(row=1,column=1)
l3=tk.Label(t,text="From email:")
l3.grid(row=2,column=0)
e3=tk.Entry(t,textvariable=s2)
e3.grid(row=2,column=1)
l4=tk.Label(t,text="To email:")
l4.grid(row=3,column=0)
e4=tk.Entry(t,textvariable=s3)
e4.grid(row=3,column=1)
l5=tk.Label(t,text="Message:")
l5.grid(row=4,column=0)
e5=tk.Entry(t,textvariable=s4)
e5.grid(row=4,column=1)

b0=tk.Button(t,text="Send",command=lambda:smtp(s0.get(),s1.get(),s2.get(),s3.get(),s4.get()))
b0.grid(row=5,column=0,columnspan=2)

b1=tk.Button(t,text="Choose and comprime image",command=lambda:img())
b1.grid(row=6,column=0,columnspan=3)

l6=tk.Label(t,text="QRCode version:")
l6.grid(row=7,column=0)
e6=tk.Entry(t,textvariable=s5)
e6.grid(row=7,column=1)
l7=tk.Label(t,text="Box size:")
l7.grid(row=8,column=0)
e7=tk.Entry(t,textvariable=s6)
e7.grid(row=8,column=1)
l8=tk.Label(t,text="Border size:")
l8.grid(row=9,column=0)
e8=tk.Entry(t,textvariable=s7)
e8.grid(row=9,column=1)
l10=tk.Label(t,text="(English) Color:")
l10.grid(row=10,column=0)
e10=tk.Entry(t,textvariable=s8)
e10.grid(row=10,column=1)
l11=tk.Label(t,text="Data:")
l11.grid(row=11,column=0)
e11=tk.Entry(t,textvariable=s9)
e11.grid(row=11,column=1)
l12=tk.Label(t,text="Naming new file:")
l12.grid(row=12,column=0)
e12=tk.Entry(t,textvariable=s10)
e12.grid(row=12,column=1)
b2=tk.Button(t,text="Generate QRCODE",command=lambda:qr(s5.get(),s6.get(),s7.get(),s8.get(),s9.get(),s10.get()))
b2.grid(row=13,column=0,columnspan=4)

t.mainloop()
