from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename,asksaveasfilename
import os
from subprocess import call

def newfile():
    global file
    root.title('untitled My - Notepad')
    file = None
    textarea.delete(1.0,END)

def openfile():
    file = askopenfilename(defaultextension = ".txt",
                           filetypes = [("All Files","*.*"),
                                        ("Text Documents","*.txt")])
    if file == '':
        file = None
    else:
        root.title(os.path.basename(file) + '- MyNotepad')
        textarea.delete(1.0,END)
        f = open(file,'r')
        textarea.insert(1.0,f.read())
        f.close()

def savefile():
    global file
    if file == None:
        file = asksaveasfilename(initialfile = 'MyNotepad',defaultextension = ".txt",
                           filetypes = [("All Files","*.*"),
                                        ("Text Documents","*.txt")])
        if file=='':
            file = None
        else:
            #save as new file
            f = open(file,'w')
            f.write(textarea.get(1.0,END))
            f.close()

            root.title(os.path.basename(file) + '- MyNotepad')
            print("File saved")
    else:
        f = open(file, 'w')
        f.write(textarea.get(1.0, END))
        f.close()

def quitApp():
    root.destroy()

def copy():
    textarea.event_generate(("<<Copy>>"))

def paste():
    textarea.event_generate(("<<Paste>>"))

def cut():
    textarea.event_generate(("<<Cut>>"))

def about():
    messagebox.showinfo(title='About My Notepad',message="Notepad by 'Rahul' on 30 Apr 2020")

def feedback():
    call(['python','feedback.py'])

if __name__ == "__main__":
    root = Tk()
    root.title('My - Notepad')
    root.wm_iconbitmap('note.ico')
    root.geometry('640x420')

    # add textarea
    textarea = Text(root,font="Arial 13")
    file = None
    textarea.pack(expand=True, fill=BOTH)

    # add menu
    menubar = Menu(root)

    # File menu starts
    filemenu = Menu(menubar, tearoff=0)

    # to create new file
    filemenu.add_command(label='New File', command=newfile)

    filemenu.add_command(label='Open file', command=openfile)

    filemenu.add_command(label='Save file', command=savefile)
    filemenu.add_separator()
    filemenu.add_command(label='Exit', command=quitApp)

    menubar.add_cascade(label='File', menu=filemenu)
    # File menu ends

    # edit menu starts

    editmenu = Menu(menubar, tearoff=0)

    editmenu.add_command(label='Copy', command=copy)
    editmenu.add_command(label='Paste', command=paste)
    editmenu.add_command(label='Cut', command=cut)

    menubar.add_cascade(label='Edit', menu=editmenu)
    # editmenu ends here

    # help menu starts
    helpmenu = Menu(menubar, tearoff=0)

    helpmenu.add_command(label='About notepad', command=about)
    helpmenu.add_command(label = 'Feed Back',command =feedback)
    menubar.add_cascade(label='Help', menu=helpmenu)
    # helpmenu ends here
    root.config(menu=menubar)

    # scrollbar
    scroll = Scrollbar(textarea)
    scroll.pack(side=RIGHT, fil=Y)
    scroll.config(command=textarea.yview)
    textarea.config(yscrollcommand=scroll.set)

    root.mainloop()