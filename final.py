import tkinter as tk
from tkinter import messagebox

def check_winner():
    global winner
    for combo in [(0,1,2), (3,4,5), (6,7,8),
                  (0,3,6), (1,4,7), (2,5,8),
                  (0,4,8), (2,4,6)]:
        if buttons[combo[0]]['text'] == buttons[combo[1]]['text'] == buttons[combo[2]]['text'] != "":
            winner = True
            for i in combo:
                buttons[i].config(bg="green")
            messagebox.showinfo("Tic-Tac-Toe", f"Player {buttons[combo[0]]['text']} wins!")
            root.quit()
            return

    
    if all(button['text'] != "" for button in buttons):
        messagebox.showinfo("Tic-Tac-Toe", "It's a Draw!")
        root.quit()

def button_click(index):
    if buttons[index]['text'] == "" and not winner:
        buttons[index]['text'] = current_player
        check_winner()
        if not winner:
            toggle_player()

def toggle_player():
    global current_player
    current_player = "O" if current_player == "X" else "X"
    label.config(text=f"Current Player: {current_player}")

root = tk.Tk()
root.title("Tic-Tac-Toe")

buttons = []
for i in range(9):
    btn = tk.Button(root, text="", font=('normal', 40), width=5, height=2,
                    command=lambda i=i: button_click(i))
    btn.grid(row=i//3, column=i%3)
    buttons.append(btn)

current_player = "X"
winner = False

label = tk.Label(root, text=f"Current Player: {current_player}'s turn", font=('normal', 20))
label.grid(row=3, column=0, columnspan=3)

root.mainloop()

