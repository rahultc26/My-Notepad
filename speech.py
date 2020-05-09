import pyttsx3
import tkinter as tk

engine = pyttsx3.init()

rate = engine.getProperty('rate')

class Widget():
    def __init__(self):
        self.root = tk.Tk()
        self.root.wm_iconbitmap('note.ico')
        self.root.title('Text To Speak')
        self.root.resizable(0, 0)
        self.label1 = tk.Label(self.root, text='Type below to speak or paste something',bg='skyblue')
        self.label1.pack()
        self.text = tk.Text(self.root,width = 40,height=10)
        self.text.config(wrap = 'word')
        self.text.pack()
        self.button = tk.Button(self.root, text='Speak!', command=self.click,bg='skyblue')
        self.button.pack()
        self.root.mainloop()

    def speak(self, text):
        newVoiceRate = 130
        while newVoiceRate <= 300:
            engine.setProperty('rate', newVoiceRate)
            engine.say(text)
            engine.runAndWait()
            newVoiceRate = newVoiceRate + 130
        engine.setProperty('rate', 500)

    def click(self):
        text = self.text.get('1.0','end')
        self.speak(text)


if __name__ == '__main__':
    widget = Widget()
