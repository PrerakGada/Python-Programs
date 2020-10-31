from tkinter import *
from tkinter import messagebox
import sqlite3

root = Tk()
root.title("Password Keeper")
root.iconbitmap('pass_icon.ico')
root.geometry("462x500")
root.resizable(0, 0)

# Frames start here

title_frame = LabelFrame(root)
title_frame.grid(row=0, column=0, padx=5)

login_frame = LabelFrame(root)
login_frame.grid(row=1, column=0, pady=50)

main_frame = LabelFrame(root, bd=0)
main_frame.grid(row=2, column=0, pady=50)

# Frames End here


conn = sqlite3.connect('pass_book.db')
c = conn.cursor()


# Functions Start Here

def show():
    conn = sqlite3.connect('pass_book.db')
    c = conn.cursor()

    show = Toplevel()
    show.geometry("400x400")
    show.resizable(0, 0)

    c.execute("SELECT *, oid FROM data")
    records = c.fetchall()

    for record in records:
        Label(show, text=record).pack()
    conn.commit()
    conn.close()


def add():
    def save():
        conn = sqlite3.connect('pass_book.db')
        c = conn.cursor()

        c.execute("INSERT INTO data VALUES (:name, :url, :username, :password)",
                  {
                      'name': name_entry.get(),
                      'url': url_entry.get(),
                      'username': username_entry.get(),
                      'password': password_entry.get()
                  })

        name_entry.delete(0, END)
        url_entry.delete(0, END)
        username_entry.delete(0, END)
        password_entry.delete(0, END)

        conn.commit()
        conn.close()

    conn = sqlite3.connect('pass_book.db')
    c = conn.cursor()

    add = Toplevel()
    add.geometry("400x400")
    add.resizable(0, 0)

    name_label = Label(add, text="Enter Name :", font="Arial 15")
    name_label.grid(row=1, column=0)

    name_entry = Entry(add, width=20)
    name_entry.grid(row=1, column=1)

    url_label = Label(add, text="Enter URL :", font="Arial 15")
    url_label.grid(row=2, column=0)

    url_entry = Entry(add, width=20)
    url_entry.grid(row=2, column=1)

    username_label = Label(add, text="Enter Username :", font="Arial 15")
    username_label.grid(row=3, column=0)

    username_entry = Entry(add, width=20)
    username_entry.grid(row=3, column=1)

    password_label = Label(add, text="Enter Password :", font="Arial 15")
    password_label.grid(row=4, column=0)

    password_entry = Entry(add, width=20)
    password_entry.grid(row=4, column=1)

    add_btn = Button(add, text="Add Password", font="Arial 20", command=save)
    add_btn.grid(row=5, column=0, columnspan=2)

    conn.commit()
    conn.close()


def delete():
    conn = sqlite3.connect('pass_book.db')
    c = conn.cursor()

    delete = Toplevel()
    delete.geometry("400x400")
    delete.resizable(0, 0)

    def dell():
        conn = sqlite3.connect('pass_book.db')
        c = conn.cursor()

        c.execute("DELETE from data WHERE oid= " + delete_entry.get())

        conn.commit()
        conn.close()

    delete_label = Label(delete, text="Enter the ID :", font="Arial 15")
    delete_label.grid(row=0, column=0)

    delete_entry = Entry(delete, width=20)
    delete_entry.grid(row=0, column=1)

    delete_btn = Button(delete, text="Delete", command=dell)
    delete_btn.grid(row=0, column=2)

    conn.commit()
    conn.close()


def edit():
    conn = sqlite3.connect('pass_book.db')
    c = conn.cursor()

    edit = Toplevel()
    edit.geometry("400x400")
    edit.resizable(0, 0)

    def update():
        conn = sqlite3.connect('pass_book.db')
        c = conn.cursor()

        def save():
            conn = sqlite3.connect('pass_book.db')
            c = conn.cursor()
            record_id = id_entry.get()
            c.execute("""UPDATE data SET
                    name = :name,
                    url = :url,
                    username = :username,
                    password = :password
                    
                    WHERE oid = :oid""",
                      {
                          'name': name_entry.get(),
                          'url': url_entry.get(),
                          'username': username_entry.get(),
                          'password': password_entry.get(),
                          'oid': record_id
                      })
            conn.commit()
            conn.close()

        name_label = Label(edit, text="Enter Name :", font="Arial 15")
        name_label.grid(row=1, column=0)

        name_entry = Entry(edit, width=20)
        name_entry.grid(row=1, column=1)

        url_label = Label(edit, text="Enter URL :", font="Arial 15")
        url_label.grid(row=2, column=0)

        url_entry = Entry(edit, width=20)
        url_entry.grid(row=2, column=1)

        username_label = Label(edit, text="Enter Username :", font="Arial 15")
        username_label.grid(row=3, column=0)

        username_entry = Entry(edit, width=20)
        username_entry.grid(row=3, column=1)

        password_label = Label(edit, text="Enter Password :", font="Arial 15")
        password_label.grid(row=4, column=0)

        password_entry = Entry(edit, width=20)
        password_entry.grid(row=4, column=1)

        edit_btn = Button(edit, text="Save Changes", font="Arial 20", command=save)
        edit_btn.grid(row=5, column=0, columnspan=2)

        record_id = id_entry.get()
        c.execute("SELECT * FROM data WHERE oid=" + record_id)
        records = c.fetchall()

        for record in records:
            name_entry.insert(0, record[0])
            url_entry.insert(0, record[1])
            username_entry.insert(0, record[2])
            password_entry.insert(0, record[3])

        conn.commit()
        conn.close()

    conn.commit()
    conn.close()

    id_label = Label(edit, text="Enter ID :", font="Arial 15")
    id_label.grid(row=0, column=0)

    id_entry = Entry(edit, width=20)
    id_entry.grid(row=0, column=1)

    id_btn = Button(edit, text="Edit", command=update)
    id_btn.grid(row=0, column=2)


def main():
    a_label = Label(main_frame, text="Choose what to do", font="Arial 20 underline")
    a_label.grid(row=0, column=0, columnspan=2)

    show_btn = Button(main_frame, text="Show all Passwords", command=show)
    show_btn.grid(row=1, column=0)

    add_btn = Button(main_frame, text="Add a new Password", command=add)
    add_btn.grid(row=1, column=1)

    del_btn = Button(main_frame, text="Delete a Password", command=delete)
    del_btn.grid(row=2, column=0)

    edit_btn = Button(main_frame, text="Edit a Password", command=edit)
    edit_btn.grid(row=2, column=1)


def submit(pas):
    conn = sqlite3.connect('pass_book.db')
    c = conn.cursor()
    c.execute("SELECT * FROM login")

    abc = c.fetchone()

    if list(abc)[0] != pas:
        messagebox.showerror("This is my Popup!", "Wrong Password!")
    else:
        main()
    admin_pass.delete(0, END)
    conn.commit()
    conn.close()


# Functions Finish Here


# Displaying the Title
Title1 = Label(title_frame, text=" Welcome to", fg="blue", font="Helvetica 19 bold")
Title2 = Label(title_frame, text="Password Keeper ", fg="red", font="System 23 bold")
Title1.grid(row=0, column=0)
Title2.grid(row=0, column=1, columnspan=2)

# Login Details
admin_pass_label = Label(login_frame, text="Enter Admin Password :", font="Arial 15")
admin_pass_label.grid(row=1, column=0)

admin_pass = Entry(login_frame, width=20)
admin_pass.grid(row=1, column=1)

submit_btn = Button(login_frame, text="Submit", font="Arial 15", command=lambda: submit(admin_pass.get()))
submit_btn.grid(row=1, column=2)

conn.commit()
conn.close()

root.mainloop()