import pyttsx3
import tkinter as tk

voiceEngine = pyttsx3.init()

rate = voiceEngine.getProperty('rate')

class Widget():
    def __init__(self):
        self.root = tk.Tk()
        self.root.wm_iconbitmap('note.ico')
        self.root.title('Text To Speak')
        self.root.resizable(0, 0)
        self.label1 = tk.Label(self.root, text='Type below to speak or paste something',bg='skyblue')
        self.label1.pack()
        self.text = tk.Text(self.root,width = 50,height=15)
        self.text.config(wrap = 'word')
        self.text.pack()
        self.button = tk.Button(self.root, text='Speak!', command=self.click,bg='skyblue')
        self.button.pack()
        self.root.mainloop()

    def speak(self, text):
        newVoiceRate = 130
        while newVoiceRate <= 300:
            voiceEngine.setProperty('rate', newVoiceRate)
            voiceEngine.say(text)
            voiceEngine.runAndWait()
            newVoiceRate = newVoiceRate + 130
        voiceEngine.setProperty('rate', 800)

    def click(self):
        text = self.text.get('1.0','end')
        self.speak(text)


if __name__ == '__main__':
    widget = Widget()
