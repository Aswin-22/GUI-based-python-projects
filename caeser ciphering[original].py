import tkinter as tk
from tkinter.font import Font
from tkinter import messagebox
from tkinter import *

import string 


def caeser_encrypt(text,shift=13):
    alpha=([string.ascii_lowercase,string.ascii_uppercase,string.punctuation])
    def shift_alpha(alpha):
        shift1=int(shift)
        return alpha[shift1:]+alpha[:shift1]

    
    shifted_alphas= tuple(map(shift_alpha,alpha))
    final_alpha=''.join(alpha)
    final_shifted_alpha=''.join(shifted_alphas)
    table=str.maketrans(final_alpha,final_shifted_alpha)
    txt4.config(text=text.translate(table))
    txt3.config(text=shifted_alphas)

def caeser_decrypt(text,shift=13):
    alpha=([string.ascii_lowercase,string.ascii_uppercase,string.punctuation])
    def shift_alpha(alpha):
        x=int(shift)
        shift1=int(26-x)
        return alpha[shift1:]+alpha[:shift1]

    
    shifted_alphas= tuple(map(shift_alpha,alpha))
    final_alpha=''.join(alpha)
    final_shifted_alpha=''.join(shifted_alphas)
    table=str.maketrans(final_alpha,final_shifted_alpha)
    txt4.config(text=text.translate(table))

def get_value1():
    x=entry.get()
    y=entry1.get()
    caeser_encrypt(x,y)
    txt2.config(text="Encryption key:")

def get_value2():
    x=entry.get()
    y=entry1.get()
    caeser_decrypt(x,y)
    txt2.config(text="Decryption key:")

def credit():
	messagebox.showinfo("CREDITS", " Aswin.M  \n Ajmal shan.C \n Syeed Ishaaq \n Muhmaad Ajmal \n Sudhakar")

def about():
	messagebox.showinfo("ABOUT", " This is a python program used to \n demonstrate caeser ciphering ")

def clr_scrn():
    entry.delete(0, END)
    entry1.delete(0, END)
    txt3.config(text="<Crypted message>")
    txt4.config(text="<Cryption key-sequence>")

root=tk.Tk()
root.title("c3s4r__boys")

root.geometry("1366x768")
root.config(bg="black")

font1=Font(family="FixedSys",size=22)
myfont=Font(family="arialblack",size=30,weight="bold")
myfont1=Font(family="ds-digital",size=32,weight="bold")
myfont2=Font(family="ds-digital",size=15,weight="bold")

title=tk.Label(root,text="CAESER CIPHER",font=myfont1,fg="cyan",bg="black")
title.place(relx=0.2,rely=0.02,relwidth=0.6)

txt1=tk.Label(root,text="Enter a message :",font=font1,fg="white",bg="black")
txt1.place(relx=-0.05,rely=0.25,relwidth=0.5)

txt2=tk.Label(root,text="cryption Key:",font=font1,fg="white",bg="black")
txt2.place(relx=-0.01,rely=0.40,relwidth=0.4)

txt3=tk.Label(root,text="<cryption key-sequence>",font=("arialblack",15),fg="white",bg="black")
txt3.place(relx=0.1,rely=0.80,relwidth=0.8)

txt4=tk.Label(root,text="<Crypted message>",font=("arialblack",15),fg="white",bg="black")
txt4.place(relx=0.25,rely=0.7,relwidth=0.5)

entry=tk.Entry(root,font=("arialblack",15))
entry.place(relx=0.32,rely=0.257,relwidth=0.4,relheight=0.04)

entry1=tk.Entry(root,font="terminal")
entry1.place(relx=0.32,rely=0.41,relwidth=0.07,relheight=0.04)

btn1=tk.Button(root,text="Encrypt",font=("arialblack",18,"bold"),fg="black",command=lambda : get_value1())
btn1.place(relx=0.37,rely=0.55,relwidth=0.1,relheight=0.07)

btn2=tk.Button(root,text="Decrypt",font=("arialblack",18,"bold"),fg="black",command=lambda : get_value2())
btn2.place(relx=0.5,rely=0.55,relwidth=0.1,relheight=0.07)

menu_bar= Menu(root)
root.config(menu=menu_bar)
sub_menu2= Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="About_project", command=about)
menu_bar.add_cascade(label="Credit", command=credit)
menu_bar.add_cascade(label="clear_screen", command=clr_scrn)

tk.mainloop()