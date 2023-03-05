import tkinter as tk
import random

# Function to print the Tic Tac Toe board
def print_board(board):
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")

# Function to check if there's a winner
def check_winner(board, player):
    if ((board[0] == player and board[1] == player and board[2] == player) or
        (board[3] == player and board[4] == player and board[5] == player) or
        (board[6] == player and board[7] == player and board[8] == player) or
        (board[0] == player and board[3] == player and board[6] == player) or
        (board[1] == player and board[4] == player and board[7] == player) or
        (board[2] == player and board[5] == player and board[8] == player) or
        (board[0] == player and board[4] == player and board[8] == player) or
        (board[2] == player and board[4] == player and board[6] == player)):
        return True
    else:
        return False

# Function to get the AI's move
def get_ai_move(board):
    available_moves = [i for i in range(9) if board[i] == " "]
    return random.choice(available_moves)

# Function to update the board in the GUI
def update_board():
    global board_buttons
    for i in range(9):
        board_buttons[i].configure(text=board[i])

# Function to handle the player's move
def handle_player_move(index):
    global board
    if board[index] == " ":
        board[index] = "X"
        update_board()
        if check_winner(board, "X"):
            tk.messagebox.showinfo("Tic Tac Toe", "Congratulations! You won!")
            window.destroy()
        elif " " not in board:
            tk.messagebox.showinfo("Tic Tac Toe", "The game is a tie.")
            window.destroy()
        else:
            handle_ai_move()

# Function to handle the AI's move
def handle_ai_move():
    global board
    ai_move = get_ai_move(board)
    board[ai_move] = "O"
    update_board()
    if check_winner(board, "O"):
        tk.messagebox.showinfo("Tic Tac Toe", "Sorry, you lost.")
        window.destroy()
    elif " " not in board:
        tk.messagebox.showinfo("Tic Tac Toe", "The game is a tie.")
        window.destroy()

# Initialize the board
board = [" "] * 9

# Create the window and board buttons
window = tk.Tk()
window.title("Tic Tac Toe")
board_buttons = []
for i in range(9):
    button = tk.Button(window, text=" ", width=5, height=2, command=lambda index=i: handle_player_move(index))
    button.grid(row=i // 3, column=i % 3)
    board_buttons.append(button)

# Start the game
handle_ai_move()

# Run the window
window.mainloop()

