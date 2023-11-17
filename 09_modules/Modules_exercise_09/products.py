import json
import tkinter as tk
from canvas import app
from helpers import clean_screen
from PIL import Image, ImageTk


def update_user(username, p_id):
    with open("database/users.txt", "r+", newline="\n") as f:
        users = [json.loads(u.strip()) for u in f]
        for user in users:
            if user["username"] == username:
                user["products"].append(p_id)
                f.seek(0)
                f.truncate()
                f.writelines([json.dumps(u) + "\n" for u in users])
                return


def update_product(p_id):
    with open("database/products.txt", "r+") as f:
        products = [json.loads(p.strip()) for p in f]
        for product in products:
            if product["id"] == p_id:
                product["count"] -= 1
                f.seek(0)
                f.truncate()
                f.writelines([json.dumps(p) + "\n" for p in products])


def buy_product(p_id):
    clean_screen()
    with open("database/current_user.txt") as f:
        username= f.read()
    if username is not None:
        update_user(username, p_id)
        update_product(p_id)

    render_products_screen()


    pass


def render_products_screen():
    clean_screen()

    with open("database/current_user.txt") as f:
        username = f.read()
    # with open("database/users.txt") as f:
    #     users = [json.loads(u.strip())for u in f]
    #     for user in users:
    #         if user["username"] == username:
    with open("database/products.txt") as f:
        products = [json.loads(p.strip())for p in f]
        for i, product in enumerate(products):
            row = i // 4 * 4
            column = i % 4
            tk.Label(app, text=product["name"]).grid(row=row, column=column)

            img = Image.open("database/images/Screenshot 2023-10-20 121158.png").resize((100, 100))
            photo_image = ImageTk.PhotoImage(img)
            image_label = tk.Label(image=photo_image)
            image_label.image = photo_image
            image_label.grid(row=row + 1, column=column)

            tk.Label(app, text=product["count"]).grid(row=row+2, column=column)
            tk.Button(app, text=f"Buy {product['id']}",
                      command=lambda p=product["id"]: buy_product(p)
                      ).grid(row=row + 3, column=column)
