import tkinter as tk
from tkinter import messagebox

board = [""] * 9

def check_winner(player):
    wins = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]

    for w in wins:
        if board[w[0]] == board[w[1]] == board[w[2]] == player:
            return True
    return False

def ai_move():
    for i in range(9):
        if board[i] == "":
            board[i] = "O"
            buttons[i].config(text="O", state="disabled")
            break

    if check_winner("O"):
        messagebox.showinfo("Game Over", "AI Wins!")
        reset_game()
    elif "" not in board:
        messagebox.showinfo("Game Over", "Match Draw!")
        reset_game()

def button_click(index):
    if board[index] == "":
        board[index] = "X"
        buttons[index].config(text="X", state="disabled")

        if check_winner("X"):
            messagebox.showinfo("Game Over", "You Win!")
            reset_game()
            return

        if "" not in board:
            messagebox.showinfo("Game Over", "Match Draw!")
            reset_game()
            return

        ai_move()

def reset_game():
    global board
    board = [""] * 9

    for btn in buttons:
        btn.config(text="", state="normal")

root = tk.Tk()
root.title("Tic Tac Toe")

buttons = []

for i in range(9):
    btn = tk.Button(
        root,
        text="",
        font=("Arial", 24),
        width=5,
        height=2,
        command=lambda i=i: button_click(i)
    )
    btn.grid(row=i//3, column=i%3)
    buttons.append(btn)

root.mainloop()