from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class FeedBack:

    def __init__(self,master):
        
        master.title('Notepad Feedback')
        master.wm_iconbitmap('note.ico')
        master.resizable(False,False)
        master.configure(background = '#b2bec3')

        self.style = ttk.Style()
        self.style.configure('TFrame',background='#b2bec3')
        self.style.configure('TLabel',background = '#b2bec3',font = ('Arial',11))
        self.style.configure('TButton',background = '#b2bec3',font = ('Arial',11))
        self.style.configure('Header.TLabel',font=('Arial',18,'bold'))
        
        
        self.frame_header = ttk.Frame(master)
        self.frame_header.pack()
        self.logo = PhotoImage(file='notepadgif.gif')
        ttk.Label(self.frame_header,image = self.logo).grid(row=0,column=0,rowspan=2)
        ttk.Label(self.frame_header,text = 'Help Me To Make Improve',style = 'Header.TLabel').grid(row=0,column=1)
        ttk.Label(self.frame_header,wraplength=320,text = "I am glad you are using My-Notepad."
                                                "Thank you for using, please help me to improve by giving feedback").grid(row=1,column=1)

        self.frame_middle = ttk.Frame(master)
        
        self.frame_middle.pack()

        ttk.Label(self.frame_middle,text = "Name:").grid(row=0,column=0,padx=5,sticky='sw')      
        ttk.Label(self.frame_middle,text = "Email:").grid(row=0,column=1,padx=5,sticky='sw')  
        ttk.Label(self.frame_middle,text = "Comments:").grid(row=2,column=0,padx=5,sticky='sw')  
        
        self.entry_name = ttk.Entry(self.frame_middle,width=20)
        self.entry_name.grid(row=1,column=0,padx=10)
        self.entry_email = ttk.Entry(self.frame_middle,width=20)
        self.entry_email.grid(row=1,column=1,padx=10)
        self.text_comments = Text(self.frame_middle,width=50,height=10)
        self.text_comments.grid(row=3,column=0,columnspan=2,padx=10)
        

        ttk.Button(self.frame_middle,text = 'Submit',command = self.submit).grid(row=4,column=0,padx=5,sticky='e')
        ttk.Button(self.frame_middle,text = 'Clear',command = self.clear).grid(row=4,column=1,padx=5,sticky='w')

        
    def submit(self):
        if len(self.entry_name.get() and self.entry_email.get()) == 0:
            messagebox.showinfo(title = 'warning',message='please enter all the details')

        elif (self.text_comments.compare("end-1c", "==", "1.0")):
            messagebox.showinfo(title = 'warning',message='please enter all the details')
            
        else:
            print('Name: {}'.format(self.entry_name.get()))
            print('Email id: {}'.format(self.entry_email.get()))
            print('Comments: {}'.format(self.text_comments.get(1.0,'end')))
            self.clear()
            messagebox.showinfo(title = 'Feedback Notice',message = 'Feedback Submitted Successfully!!')

    def clear(self):
        self.entry_name.delete(0,'end')
        self.entry_email.delete(0,'end')
        self.text_comments.delete(1.0,'end')
        


def main():
    root = Tk()
    feedback = FeedBack(root)
    root.mainloop()

if __name__ == "__main__":main()
