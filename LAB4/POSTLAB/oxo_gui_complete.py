import tkinter as tk
import tkinter.messagebox as mb
from tkinter import filedialog
import oxo_logic

top = tk.Tk()
game = None  # Global game object

def buildMenu(parent):
    menus = (
        ("File", (("New", evNew),
                  ("Resume", evResume),
                  ("Save", evSave),
                  ("Exit", evExit))),
        ("Help", (("Help", evHelp),
                  ("About", evAbout)))
    )
    menubar = tk.Menu(parent)
    for menu in menus:
        m = tk.Menu(parent)
        for item in menu[1]:
            m.add_command(label=item[0], command=item[1])
        menubar.add_cascade(label=menu[0], menu=m)
    return menubar

def evNew():
    global game
    game = oxo_logic.Game()
    status['text'] = "Playing game"
    game2cells(game.board)

def evResume():
    global game
    filename = filedialog.askopenfilename(
        title="Open Saved Game",
        filetypes=(("Data Files", "*.dat"), ("All Files", "*.*"))
    )
    if filename:
        game = oxo_logic.Game()
        game.loadFromFile(filename)
        status['text'] = "Playing game"
        game2cells(game.board)

def evSave():
    global game
    filename = filedialog.asksaveasfilename(
        title="Save Game As",
        defaultextension=".dat",
        filetypes=(("Data Files", "*.dat"), ("All Files", "*.*"))
    )
    if filename:
        game.saveToFile(filename)

def evExit():
    if status['text'] == "Playing game":
        if mb.askyesno("Quitting", "Do you want to save the game before quitting?"):
            evSave()
    top.quit()

def evHelp():
    mb.showinfo("Help", '''
File -> New: Starts a new game of Tic-Tac-Toe
File -> Resume: Opens a saved game
File -> Save: Saves the current game
File -> Exit: Quits the game (prompts to save if in progress)
Help -> Help: Shows this help dialog
Help -> About: Shows program information
''')

def evAbout():
    mb.showinfo("About", "Tic-Tac-Toe GUI demo by Alan Gauld\nModified with GUI enhancements")

def evClick(row, col):
    global game
    if status['text'] == "Game over":
        mb.showerror("Game over", "The game is already over!")
        return

    index = (3 * row) + col
    result = game.userMove(index)

    if result is None:
        return  # Invalid move

    game2cells(game.board)

    if not result:
        result = game.computerMove()
        game2cells(game.board)

    if result == "D":
        mb.showinfo("Result", "It's a Draw!")
        status['text'] = "Game over"
    elif result in ["X", "O"]:
        mb.showinfo("Result", f"The winner is: {result}")
        status['text'] = "Game over"

def game2cells(board_data):
    table = board_frame.pack_slaves()[0]
    for row in range(3):
        for col in range(3):
            table.grid_slaves(row=row, column=col)[0]['text'] = board_data[3 * row + col]

def cells2game():
    values = []
    table = board_frame.pack_slaves()[0]
    for row in range(3):
        for col in range(3):
            values.append(table.grid_slaves(row=row, column=col)[0]['text'])
    return values

def buildBoard(parent):
    outer = tk.Frame(parent, border=2, relief="sunken")
    inner = tk.Frame(outer)
    inner.pack()
    for row in range(3):
        for col in range(3):
            cell = tk.Button(inner, text=" ", width=5, height=2,
                             command=lambda r=row, c=col: evClick(r, c))
            cell.grid(row=row, column=col)
    return outer

# Build UI
mbar = buildMenu(top)
top["menu"] = mbar

board_frame = buildBoard(top)
board_frame.pack()

status = tk.Label(top, text="Playing game", border=0, background="lightgrey", foreground="red")
status.pack(anchor="s", fill="x", expand=True)

# Start game
evNew()

top.mainloop()
