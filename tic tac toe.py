import tkinter as tk
from tkinter import messagebox, simpledialog

# Initialize main window
root = tk.Tk()
root.title("Tic Tac Toe")

# Ask for player names at the start
player_X_name = simpledialog.askstring("Player Name", "Enter name for Player X:")
player_O_name = simpledialog.askstring("Player Name", "Enter name for Player O:")

if not player_X_name:
    player_X_name = "Player X"
if not player_O_name:
    player_O_name = "Player O"

# Game variables
current_player = "X"
board = [""] * 9
buttons = []
score_X = 0
score_O = 0

# Labels for scoreboard
label_X = tk.Label(root, text=f"{player_X_name}: 0", font=("Arial", 14), fg="red")
label_X.grid(row=0, column=0, columnspan=1)

label_O = tk.Label(root, text=f"{player_O_name}: 0", font=("Arial", 14), fg="blue")
label_O.grid(row=0, column=2, columnspan=1)

def update_scoreboard():
    label_X.config(text=f"{player_X_name}: {score_X}")
    label_O.config(text=f"{player_O_name}: {score_O}")

def check_winner():
    wins = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
        (0, 4, 8), (2, 4, 6)              # diagonals
    ]
    for a, b, c in wins:
        if board[a] == board[b] == board[c] != "":
            return board[a]
    if "" not in board:
        return "Tie"
    return None

def button_click(i):
    global current_player, score_X, score_O
    if board[i] == "":
        board[i] = current_player
        if current_player == "X":
            buttons[i].config(text=current_player, fg="red", bg="lightyellow")
        else:
            buttons[i].config(text=current_player, fg="blue", bg="lightgreen")
        
        winner = check_winner()
        if winner:
            if winner == "Tie":
                messagebox.showinfo("Game Over", "It's a Tie!")
            else:
                winner_name = player_X_name if winner == "X" else player_O_name
                messagebox.showinfo("Game Over", f"{winner_name} wins!")
                if winner == "X":
                    score_X += 1
                else:
                    score_O += 1
                update_scoreboard()
            reset_board()
        else:
            current_player = "O" if current_player == "X" else "X"

def reset_board():
    global board, current_player
    board = [""] * 9
    current_player = "X"
    for btn in buttons:
        btn.config(text="", fg="black", bg="SystemButtonFace")

# Create 3x3 grid of buttons (start at row 1 to leave space for scoreboard)
for i in range(9):
    btn = tk.Button(root, text="", font=("Arial", 24), width=5, height=2,
                    command=lambda i=i: button_click(i))
    btn.grid(row=(i//3)+1, column=i%3)  # +1 so grid starts below scoreboard
    buttons.append(btn)

root.mainloop()