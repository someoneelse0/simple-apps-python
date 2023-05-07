# -*- encoding: utf-8 -*-
#!/usr/bin/python3

import sqlite3 as sql, tkinter as tk, os
from passlib.hash import argon2

def f0(a,b):
	con=sql.connect("z.sqlite3")
	cur=con.cursor()
	l=os.listdir()
	if ["z.sqlite3"] not in l:
		cur.execute("CREATE TABLE t0(username, keykey);")
	p=argon2.using(salt=b"0t1u2v3w4x5y6z7A",rounds=128).hash(b)
	cur.execute("INSERT INTO t0(username, keykey) VALUES('"+a+"','"+p+"');")
	con.commit()
	r=cur.execute("SELECT username, keykey from t0;")
	con.close()

def app():
	t=tk.Tk()
	t.title("Log in")

	s0=tk.StringVar()
	s1=tk.StringVar()
	s2=tk.StringVar()

	l0=tk.Label(t,text="Username:")
	l0.grid(row=0,column=0)
	e0=tk.Entry(t,textvariable=s0)
	e0.grid(row=0,column=1,padx=10,pady=10)
	l0=tk.Label(t,text="Key:")
	l0.grid(row=1,column=0)
	e1=tk.Entry(t,textvariable=s1)
	e1.grid(row=1,column=1,padx=10,pady=10)
	b0=tk.Button(t,text="Send",command=lambda:f0(s0.get(),s1.get()))
	b0.grid(row=2,column=0,columnspan=2,padx=10,pady=10)

	t.mainloop()

if __name__=="__main__":
	app()
