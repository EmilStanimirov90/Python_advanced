import tkinter as tk

app_config = {
    'board': [[None] * 3 for _ in range(3)],
    'buttons': [[None] * 3 for _ in range(3)],
    'sign': "X",
    'X': None,
    "O": None
}


def render_board(window_):
    grid_frame = tk.Frame(master=window_)
    grid_frame.pack()
    for row in range(3):
        for col in range(3):
            app_config["buttons"][row][col] = tk.Button(
                master=grid_frame,
                text= "x "
            )


def start_game(window_, player_one_):
    window_.destroy()
    window_ = tk.Tk()
    window_.geometry("240x240")
    window_.title("Tic Tac Toe")

    pass


def start_screen():
    window = tk.Tk()
    window.geometry("240x240")
    window.title("Tic Tac Toe")
    window.configure()

    tk.Label(window, text="First player name: ").pack()
    player_one = tk.Entry(window)
    player_one.pack()
    tk.Label(window, text="Second player name: ").pack()
    player_two = tk.Entry(window)
    player_two.pack()

    tk.Button(window, text="Start game", command=lambda: start_game(window, player_one)).pack()

    window.mainloop()
    pass


if __name__ == '__main__':
    start_screen()
