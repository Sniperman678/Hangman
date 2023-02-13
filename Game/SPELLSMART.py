#Tkinter it is a GUI

import os
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

#Directions

E=tk.E
W=tk.W
N=tk.N
S=tk.S

#variables

q = 0
s = -1
count = 0
correct = 0
incorrect = 0
asdf = TRUE

#Various Arrays: words, pictures and answers

pics = ["apple.png","ball.png","cup.png","dog.png","egg.png","frog.png","goat.png","hat.png","ice.png","kite.png","lips.png","milk.png","nest.png","owl.png","pan.png","rose.png","sad.png","tent.png","umbrella.png","van.png","water.png","xray.png","zebra.png"]
question = ["How do you spell this picture"]
answer = ["apple","ball","cup","dog","egg","frog","goat","hat","ice","kite","lips","milk","nest","owl","pan","rose","sad","tent","umbrella","van","water","xray","zebra"]
words = ["CORRECT","INCORRECT"]

def getWindow():
    if(asdf == TRUE):
        return(selectWindow(root))
    else:
        return(gameWindow(root))

#quiting program

def quitProgram():
    root.destroy()

def selectUser(select):
    if select == False:
        return(selectWindow(root))
    elif select == True:
        return(gameWindow(root))

class selectWindow(tk.Frame):
    def __init__(self, master=None):
        ttk.Frame.__init__(self, master)
        self.grid(sticky=N+S+E+W)

        top = self.winfo_toplevel()
        top.rowconfigure(2, weight=1)
        top.columnconfigure(3, weight=1)

        self.rowconfigure(3, weight=1)
        self.columnconfigure(3, weight=1)
        self.__createWidgets()

    def logout(self):
        global asdf
        print(asdf)
        asdf = FALSE
        print(asdf)
        self.destroy()
        getWindow()

#instructions for the game

    def showInstructions(self):
        self.d.config(text="How to Play: A picture will apear in the middle of the screen and you  will attempt to spell it correctly and once spelt word click Submit. Enjoy")

#buttons for the start screen

    def __createWidgets(self):
        self.a = tk.Button(self, text='Play Game',command=self.logout)
        self.a.grid(row=1, column=2) #, sticky=N+S+E+W)
        self.c = tk.Button(self, text='How To Play', command=self.showInstructions)
        self.c.grid(row=2, column=2)
        self.b = tk.Button(self, text='Quit',command=quitProgram)
        self.b.grid(row=3, column=2) #, sticky=N+S+E+W)
        self.d = tk.Label(self, text='')
        self.d.grid(row=4, column=2, sticky=N+S+E+W)

class gameWindow(tk.Frame):
    def __init__(self, master=None):
        ttk.Frame.__init__(self, master)
        self.grid(sticky=N+S+E+W)

        top = self.winfo_toplevel()
        top.rowconfigure(6, weight=1)
        top.columnconfigure(6, weight=1)

        self.rowconfigure(6, weight=1)
        self.columnconfigure(6, weight=1)
        self.__createWidgets()

#labels and buttons for the game

    def __createWidgets(self):
        self.name = tk.Label(self,text = "SpellSmart")
        self.name.grid()
        self.img = tk.PhotoImage(file=pics[q])
        self.panel = tk.Label(self, image=self.img)
        self.panel.grid()
        self.label = tk.Label(self,text = question[0])
        self.label.grid()
        self.label2 = tk.Label(self,text = "---")
        self.label2.grid()
        self.entry = tk.Entry(self)
        self.entry.grid()
        self.button = tk.Button(self,text = "Submit",command=self.out)
        self.button.grid()
        self.button_two = tk.Button(self,text = "Restart",command=self.stop)
        self.button_two.grid()

#Closing the program

    def logout(self):
        self.destroy()
        selectUser()

#point system number of correct and incorrect

    def out(self):
        global q,correct,incorrect,s,count
        count = count + 1
        print (answer)
        print (question[0])
        print (answer[q])
        ans = self.entry.get()
        if count < len(answer):
            if answer[q] == ans:
                q = q + 1
                self.entry.delete(0, END)
                correct = correct + 1
                self.label.config(text = question[0])
                self.label2.config(text = words[0])
            else:
                q = q + 1
                self.entry.delete(0, END)
                incorrect = incorrect + 1
                self.label.config(text = question[0])
                self.label2.config(text = words[1])
            self.img.config(file=pics[q])
            self.panel.config(image=self.img)
        else:
            self.entry.delete(0, END)
            self.label.config(text = "Correct: "+str(correct) + " Incorrect:   "+str(incorrect))

    def stop(self):
        global q,correct,incorrect
        q = 0
        correct = 0
        incorrect = 0
        self.entry.delete(0, END)
        self.label.config(text = question[0])

if __name__ == "__main__":
    root=Tk()
    m=getWindow()
    root.title("SpellSmart")
    root.mainloop()