import tkinter as tk
from tkinter import filedialog, Text
import os



root = tk.Tk()
root.title("Duplicate Remover (By Leon990x)")
root.resizable(width=False, height=False)
root.configure(background="grey")
root.geometry("600x600")

def addApp():
	try:
	    for widget in frame.winfo_children():
	        widget.destroy()

	    #selected file into filename
	    filename = filedialog.askopenfilename(initialdir="/", title="Select File", filetypes=(("text files", "*.txt"), ("all files", "*.*")))
	    name = str(os.path.basename(filename))
	    label = tk.Label(frame, text = filename, bg = "white")
	    label.pack()
	    check(name)
	except:
		error = tk.Tk()
		error.title("Fatal Error Occurred")
		error.resizable(width=False, height=False)
		error.geometry("500x200")
		msg = tk.Label(error, text = "Pufise couldn't understand your file. Please open another one.", bg = "white")
		msg.pack()

def undo(backup, original):
	f = open(original, "w")
	backup = open(backup, "r")
	backup = backup.readlines()
	for i in backup:
		f.write(i)


def generate(name, Names, button):
	out_file = open(name, "r")
	f = out_file.readlines()
	backup = open("temp.txt", "w")
	for j in f:
		backup.write(j)
	backup.close()
	out_file.close()


	out_file = open(name, "w")
	for k in set(Names):
		out_file.write(k+"\n")
	out_file.close()
	button.grid_forget()
	cleaned = tk.Label(frame, text = "\n\nRemoved Duplicates!\n", bg = "white")
	cleaned.pack()

	undo1 = tk.Button(root, text="Undo Action", padx = 10, pady = 5, fg = "white", bg = "red", command = lambda: undo("temp.txt", name))
	undo1.grid(row=0,column=2)

def check(name):
    Names = []
    repeats = []
    for line in open(name,'r').readlines():
        Names.append(line.strip())
    for i in range(len(Names)):
        Names[i] = Names[i].lower()
    for j in range(len(Names)):
        if Names.count(Names[j]) != 1:
            repeats.append(Names[j])
    
    repeats = set(repeats)
    repeats = list(repeats)
    repeats.sort()
    if len(repeats) != 0:
        label2 = tk.Label(frame, text = "\n\nDuplicates found:\n", bg = "white")
        label2.pack()
        for i in repeats:
            label3 = tk.Label(frame, text = i, bg = "white")
            label3.pack()

        chkFile = tk.Button(root, text="Remove Duplicates for " + name, padx = 10, pady = 5, fg = "black", bg = "lightgrey", command = lambda: generate(name, Names, chkFile))
        chkFile.grid(row=0,column=2)

    else:
            label4 = tk.Label(frame, text = "\n\nNo Duplicates Found!\n", bg = "white")
            label4.pack()
    return name

# canvas = tk.Canvas(root, height = 600, width = 600, bg = "grey")
openFile = tk.Button(root, text="Open File", padx = 10, pady = 5, fg = "black", bg = "lightgrey", command = addApp)
openFile.grid(row=0,column=1)
# canvas.pack()


frame = tk.Frame(root, bg = "white")
tk.Label(frame, 
		 text="INSTRUCTIONS\n",
		 fg = "black",
		 bg = "white",
		 font = "Helvetica 16 bold").pack(side = 'top')
tk.Label(frame, 
		 text="Open a text file (.txt) \n to determine whether or not \n the file contains duplicate lines",
		 fg = "black",
		 bg = "white",
		 font = "Helvetica 16").pack()
frame.place(relwidth = 0.8, relheight = 0.8, relx = 0.1, rely=0.1)


# openFile = tk.Button(canvas, text="Open File", padx = 10, pady = 5, fg = "white", bg = "grey", command = addApp)
# openFile.pack(side = "top")


root.mainloop()


