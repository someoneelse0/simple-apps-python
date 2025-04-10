#!/usr/bin/python3
# -*- encoding: utf-8 -*-

import sqlite3 as sql, tkinter as tk
from argon2 import PasswordHasher

ph = PasswordHasher()

def f0(username, password):
    con = sql.connect("z.sqlite3")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS t0(username TEXT, keykey TEXT);")

    hashed = ph.hash(password)

    cur.execute("INSERT INTO t0(username, keykey) VALUES(?, ?);", (username, hashed))
    con.commit()
    con.close()

def app():
    t = tk.Tk()
    t.title("Sign Up")

    s0 = tk.StringVar()
    s1 = tk.StringVar()
    tk.Label(t, text="Username:").grid(row=0, column=0, padx=10, pady=10)
    tk.Entry(t, textvariable=s0).grid(row=0, column=1)

    tk.Label(t, text="Password:").grid(row=1, column=0, padx=10, pady=10)
    tk.Entry(t, textvariable=s1, show="*").grid(row=1, column=1)

    tk.Button(t, text="Sign Up", command=lambda: f0(s0.get(), s1.get())).grid(row=2, column=0, columnspan=2, pady=10)

    t.mainloop()

if __name__ == "__main__":
    app()
