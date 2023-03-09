import tkinter as tk
import TicTacToe
import RPS
def open_new_window():
    new_window = tk.Toplevel()
    new_window.title("New Window")
    new_window.geometry("400x400")
    new_window.configure(bg="lightblue")

root = tk.Tk()
root.title("Main Window")
root.geometry("400x400")
root.configure(bg="lightgray")

tic_tac_toe_button = tk.Button(root, text="Play tic tac toe",bg="lightblue",font=("Georgia",16), command=TicTacToe.play, width=20, height=3, bd=3, relief="raised")
tic_tac_toe_button.pack()

rock_paper_scissors_button = tk.Button(root, text="Play rock paper scissors",bg="lightblue",font=("Georgia",16), command=RPS.create_gui, width=20, height=3, bd=3, relief="raised")
rock_paper_scissors_button.pack()

root.mainloop()
