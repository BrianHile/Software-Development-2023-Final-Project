import tkinter as tk
import TicTacToe
import RPS

def open_new_window():
    new_window = tk.Toplevel()
    new_window.title("New Window")

root = tk.Tk()
root.title("Main Window")

tic_tac_toe_button = tk.Button(root, text="Play tic tac toe", command=TicTacToe.play)
tic_tac_toe_button.pack()

rock_paper_scissors_button = tk.Button(root, text="Play rock paper scissors", command=RPS.create_gui)
rock_paper_scissors_button.pack()

root.mainloop()
