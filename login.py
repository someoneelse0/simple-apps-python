#!/usr/bin/python3
# -*- encoding: utf-8 -*-

import sqlite3 as sql, tkinter as tk
from argon2 import PasswordHasher, exceptions as argon2_exceptions

ph = PasswordHasher()

def f0(username, password, t):
    con = sql.connect("z.sqlite3")
    cur = con.cursor()

    cur.execute("SELECT keykey FROM t0 WHERE username = ?;", (username,))
    row = cur.fetchone()
    con.close()

    result_label = tk.Label(t, text="Verified:")
    result_label.grid(row=3, column=0)

    if row:
        try:
            ph.verify(row[0], password)
            verified = tk.Label(t, text="True", fg="green")
        except argon2_exceptions.VerifyMismatchError:
            verified = tk.Label(t, text="False", fg="red")
    else:
        verified = tk.Label(t, text="User not found", fg="orange")
    verified.grid(row=3, column=1)

def app():
    t = tk.Tk()
    t.title("Log In")

    s0 = tk.StringVar()
    s1 = tk.StringVar()

    tk.Label(t, text="Username:").grid(row=0, column=0, padx=10, pady=10)
    tk.Entry(t, textvariable=s0).grid(row=0, column=1)

    tk.Label(t, text="Password:").grid(row=1, column=0, padx=10, pady=10)
    tk.Entry(t, textvariable=s1, show="*").grid(row=1, column=1)

    tk.Button(t, text="Log In", command=lambda: f0(s0.get(), s1.get(), t)).grid(row=2, column=0, columnspan=2, pady=10)

    t.mainloop()

if __name__ == "__main__":
    app()
