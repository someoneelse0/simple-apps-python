# -*- encoding: utf-8 -*-
#!/usr/bin/python3

import sqlite3 as sql, tkinter as tk, os
from passlib.hash import argon2

def f0(a,b,t):
	con=sql.connect("z.sqlite3")
	cur=con.cursor()
	rr=cur.execute("SELECT username, keykey FROM t0 WHERE username='"+a+"';").fetchall()
	con.close()
	l2=tk.Label(t,text="Verified:")
	l2.grid(row=3,column=0)
	tf=argon2.verify(b,rr[0][1])
	l3=""
	if tf:
		l3=tk.Label(t,text="True")
	else:
		l3=tk.Label(t,text="False")
	l3.grid(row=3,column=1)

def app():
	t=tk.Tk()
	t.title("Log in")

	s0=tk.StringVar()
	s1=tk.StringVar()

	l0=tk.Label(t,text="Username:")
	l0.grid(row=0,column=0,padx=10,pady=10)
	e0=tk.Entry(t,textvariable=s0)
	e0.grid(row=0,column=1,padx=10,pady=10)
	l1=tk.Label(t,text="Key:")
	l1.grid(row=1,column=0,padx=10,pady=10)
	e1=tk.Entry(t,textvariable=s1)
	e1.grid(row=1,column=1,padx=10,pady=10)
	b0=tk.Button(t,text="Send",command=lambda:f0(s0.get(),s1.get(),t))
	b0.grid(row=2,column=0,columnspan=2)

	t.mainloop()

if __name__=="__main__":
	app()
