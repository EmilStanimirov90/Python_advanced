import tkinter as tk
import json
from canvas import app
from helpers import clean_screen
from products import render_products_screen
from string import punctuation,ascii_uppercase, ascii_lowercase, digits

def register(**user):
    if user['username'] == "" or user['password'] == '' or user['firstname'] == '' or user['last_name'] == "":
        render_register_screen(error="All fields are required!")
        return
    if len(user['username']) < 4:
        render_register_screen(error="Username must have more than 3 characters!")
        return
    if len(user['password']) < 4:
        render_register_screen(error="Password must have more than 3 characters!")
        return
    pass_validation_mapper = {"upper": False, "lower": False, 'digit': False, "special": False}
    for ch in user['password']:
        if ch in ascii_uppercase:
            pass_validation_mapper['upper'] = True
        elif ch in ascii_lowercase:
            pass_validation_mapper["lower"] = True
        elif ch in digits:  
            pass_validation_mapper['digit'] = True
        elif ch in punctuation:
            pass_validation_mapper['special'] = True
    if not all(pass_validation_mapper.values()):
        render_register_screen(error="Password must have upper, lower, digit and special character")
        return



    user.update({'products': []})
    with open("database/user.credentials_db.txt", "r+", newline='\n') as file:
        users = [line.strip().split(",")[0] for line in file]
        if user['username'] in users:
            render_register_screen(error="User already exists")
            return
        file.write(f"{user['username']}, {user['password']}\n")
    with open("database/users.txt", "a", newline="\n") as file:
        file.write(json.dumps(user) + "\n")
    render_login_screen()


def login(username, password):
    with open("database/user.credentials_db.txt") as file:
        data = file.readlines()
        for line in data:
            name, pwd = line.strip().split(", ")
            if username == name and password == pwd:
                with open("database/current_user.txt", "w") as f:
                    f.write(name)
                render_products_screen()
                return

    render_login_screen(error="Invalid username or password")


def render_login_screen(error=None):
    clean_screen()
    username = tk.Entry(app)
    username.grid(row=0, column=0)
    password = tk.Entry(app)
    password.grid(row=1, column=0)

    if error is not None:
        tk.Label(app, text=error).grid(row=3, column=0)

    tk.Button(app, text="Enter", bg="green", fg="white",
              command=lambda: login(username.get(), password.get())).grid(row=4, column=0)


def render_register_screen(error=None):
    clean_screen()
    username = tk.Entry(app)
    username.grid(row=0, column=0)
    password = tk.Entry(app)
    password.grid(row=1, column=0)
    firstname = tk.Entry(app)
    firstname.grid(row=2, column=0)
    last_name = tk.Entry(app)
    last_name.grid(row=3, column=0)

    if error is not None:
        tk.Label(app, text=error).grid(row=5, column=0)

    tk.Button(app,
              text="Enter",
              bg="green",
              fg="white",
              command=lambda: register(
                  username=username.get(),
                  password=password.get(),
                  firstname=firstname.get(),
                  last_name=last_name.get())
              ).grid(row=4, column=0)


def render_main_enter_screen():
    tk.Button(app, text="Login", bg="green", fg="white", command=render_login_screen).grid(row=0, column=0)
    tk.Button(app, text="Register", bg="yellow", fg="black", command=render_register_screen).grid(row=0, column=1)

    pass
