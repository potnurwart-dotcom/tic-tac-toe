import tkinter as tk

def button_click(index):
    buttons[index].config(text="X")
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