import tkinter as tk
from tkinter import ttk
from tkinter import font,colorchooser,messagebox
win=tk.Tk()
win.title("TEXT EDITOR 2")
# win.geometry("1200*800")
menubar=tk.Menu(win)

# open_icon=tk.PhotoImage(r".spyder-py3\save")
# save_as_icon=tk.PhotoImage(r".spyder-py3\save")
# exit_icon=tk.PhotoImage(r".spyder-py3\save")
new_icon=tk.PhotoImage(file="save.png")
# save_icon=tk.PhotoImage(r"save.png")
file_menu=tk.Menu(menubar,tearoff=0)
file_menu.add_command(label="New",image=new_icon)
edit_menu=tk.Menu(menubar,tearoff=0)
View_menu=tk.Menu(menubar,tearoff=0)
colour_menu=tk.Menu(menubar,tearoff=0)
menubar.add_cascade(label="FILE",menu=file_menu)
menubar.add_cascade(label="EDIT",menu=edit_menu)
menubar.add_cascade(label="View",menu=View_menu)
menubar.add_cascade(label="Colour",menu=colour_menu)
win.configure(menu=menubar) 

win.mainloop()
