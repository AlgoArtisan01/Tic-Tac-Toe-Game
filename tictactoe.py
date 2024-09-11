from tkinter import *
from tkinter import messagebox
import random as r

def button(frame):  # Function to define a button
    b = Button(frame, padx=1, bg="#1f1f1f", fg="white", width=3, text="   ", font=('arial', 60, 'bold'), relief="sunken", bd=10)
    return b

def change_a():  # Function to change the player for the next turn
    global a
    a = 'O' if a == 'X' else 'X'

def reset():  # Resets the game
    global a
    for i in range(3):
        for j in range(3):
            b[i][j]["text"] = " "
            b[i][j]["state"] = NORMAL
    a = r.choice(['O', 'X'])
    label.config(text=a + "'s Turn")

def check():  # Checks for victory or draw
    for i in range(3):
        if (b[i][0]["text"] == b[i][1]["text"] == b[i][2]["text"] == a or
            b[0][i]["text"] == b[1][i]["text"] == b[2][i]["text"] == a):
            messagebox.showinfo("Victory!", "'" + a + "' has won!")
            reset()
            return
    
    if (b[0][0]["text"] == b[1][1]["text"] == b[2][2]["text"] == a or
        b[0][2]["text"] == b[1][1]["text"] == b[2][0]["text"] == a):
        messagebox.showinfo("Victory!", "'" + a + "' has won!")
        reset()
        return

    elif all(b[i][j]["state"] == DISABLED for i in range(3) for j in range(3)):
        messagebox.showinfo("Tied!", "The match ended in a draw.")
        reset()

def click(row, col):
    b[row][col].config(text=a, state=DISABLED, disabledforeground=colour[a])
    check()
    change_a()
    label.config(text=a + "'s Turn")

###############   Main Program #################

root = Tk()  # Window defined
root.title("Tic-Tac-Toe")  
root.configure(bg="#333333")  
a = r.choice(['O', 'X'])  # Randomly select who goes first
colour = {'O': "#ff4d4d", 'X': "#66ff66"}  

b = [[], [], []]
for i in range(3):
    for j in range(3):
        b[i].append(button(root))
        b[i][j].config(command=lambda row=i, col=j: click(row, col))
        b[i][j].grid(row=i, column=j)

label = Label(root, text=a + "'s Turn", font=('arial', 20, 'bold'), bg="#333333", fg="white")
label.grid(row=3, column=0, columnspan=3)

root.mainloop()
