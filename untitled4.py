# -*- coding: utf-8 -*-
"""
Created on Sat Jul 31 08:21:55 2021

@author: joyab
"""

from tkinter import *

root=Tk()
root.title("Encryption with Ascii code")

root.geometry("400x400")
root.configure(background = 'snow')

enter_word = Entry(root)
enter_word.place(relx=0.5,rely=0.4, anchor = CENTER)

label = Label(root, text = "Name in Ascii :", bg="light yellow", fg="black")
label2 = Label(root, text = "Encrypted Name: ", bg="light blue", fg ="black")

def asciiConverter():
    input_word = str(enter_word.get())
    
    for letter in input_word :
        label["text"] += str(ord(letter)) + " "
        ascii=int(ord(letter))
        encrypted = ascii-1
        label2["text"] += str(chr(encrypted))
btn=Button(root, text="Display Ascii code and Encrypted value", command=asciiConverter, bg='gold', fg ='black')
btn.place(relx=0.5, rely=0.5,anchor=CENTER)

label.place(relx=0.5, rely=0.6,anchor=CENTER)
label2.place(relx=0.5, rely=0.7,anchor=CENTER)
root.mainloop()