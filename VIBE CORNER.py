import tkinter as tk
from tkinter import * 
from tkinter.font import Font
import tkinter.ttk as ttk
import time as tf
from time import strftime
from time import *
from tkinter import filedialog
from tkinter import messagebox
import pygame
import os
import sys
from datetime import date
from mutagen.mp3 import MP3
import pyttsx3


#CREATING TKINTER WINDOW
root=tk.Tk()
#COLORS TO BE USED 
w="#D7D7CB"
k="black"
g="green"
b="blue"
r="red"

#TKINTER WINDOW TITLE
root.title("VIBE CORNER")

#FONT STYLES TO BE USED
myfont=Font(family="ds-digital",size=13,weight="bold")
bladefont=Font(family="Blade 2",size=30)

#INITIATING PYGAME.MIXER
pygame.init()

#INITATING PYGAME.MIXER
pygame.mixer.init()


#SONG FOLDER SELECTION
def browse():
    global filename
    #OPENING DAILOUGE BOX TO SELECT FOLDER/DIRECTORY    
    filename = filedialog.askdirectory()

    #TO CHANGE CURRENT RUNNING PROGRAM TO SELECTED FOLDER/DIRECTORY 
    os.chdir(filename)

    #STORING FILE NAMES IN A VARIABLE 'x' IN A LIST FORM
    x=os.listdir(filename)

    #ADDING EACH FILE TO SONG_LIST__BOX 
    for s in x:
        list_box.insert(END,s)


#PLAY    
def play_button():
    #RECIEVING THE SONG SELECTED 
    cursong=list_box.get(ACTIVE)

    #CURRENT WORKING DIRECTORY
    z=os.getcwd()

    #STRUCTURE OF SONG ADDRESS
    structofsong=z+"\\"+cursong

    #LOADING SONG 
    pygame.mixer.music.load(structofsong)
    
    #PLAYS THE LOADED SONG
    pygame.mixer.music.play(loops=0)
    
#PAUSE_MUSIC DEFAULT STATE     
pause_music = False

#PAUSE
def pause_button():
    global pause_music
    #PAUSE MUSIC
    if pause_music:
        pygame.mixer.music.unpause()
        pause_music = False
    
    #UNPAUSE THE SONG AFTER BEIGN PAUSED 
    else:
        pygame.mixer.music.pause()
        pause_music = True

#STOP 
def stop_button():
    #DEFAULT STATUS OF PAUSE MUSIC CHANGED
	pause_music =False

    #SONG STOPS
	pygame.mixer.music.stop()


#PLAY NEXT SONG IN LIST
def NEXT__SONG():
    #GET THE CURRENT SONG TUPLE NUMBER
    next=list_box.curselection()

    #ADD INDEX VALUE TO THE CURRENT SONG NUMBER
    next=next[0]+1

    #RECIEVE SONG TITLE FROM SONG_LIST
    song=list_box.get(next)

    #LOAD AND PLAY SONG
    z=os.getcwd()
    structofsong=z+"\\"+song 
    pygame.mixer.music.load(structofsong)
    pygame.mixer.music.play(loops=0)

    #CLEAR ACTIVATE BAR IN SONG_LIST
    list_box.selection_clear(0, END)

    #ACTIVATE SONG IN NEXT INDEX IN SONG_LIST
    list_box.activate(next)

    #SETTING ACTIVATION TO NEXT SONG
    list_box.selection_set(next, last=None)

#PREVIOUS SONG
def PREVIOUS__SONG():
    #GET THE CURRENT SONG TUPLE NUMBER
    previous=list_box.curselection()

    #REMOVE INDEX VALUE TO THE CURRENT SONG NUMBER TO MOVE BACK IN LIST
    previous=previous[0]-1

    #RECIEVE SONG TITLE FROM SONG_LIST
    song=list_box.get(previous)

    #LOAD AND PLAY SONG
    z=os.getcwd()
    structofsong=z+"\\"+song 
    
    pygame.mixer.music.load(structofsong)
    pygame.mixer.music.play(loops=0)

    #CLEAR ACTIVATE BAR IN SONG_LIST
    list_box.selection_clear(0, END)

    #ACTIVATE SONG IN PREVIOUS INDEX IN SONG_LIST
    list_box.activate(previous)

    #SETTING ACTIVATION TO PREVIOUS SONG
    list_box.selection_set(previous, last=None)

#REPEAT
def repeatbtn():
    pygame.mixer.music.play(-1)

#MENU BAR FUNCTIONS 
def credit():
	messagebox.showinfo("CREDITS", " Aswin.M  \n Tharun.V.M  \n Nitheesh.N  \n Srinivas.S  ")

def about():
	messagebox.showinfo("About Us", "Welcome to VIBE CORNER.This is a platform which provides you with easy access to your favourite tunes! So sit back or dance along with VIBE CORNER!")

#DARK MODE__BUTTON DEFAULT STATUS
btnState= False

# DARKMODE SWITCH CONDITIONS 
def switch():
    global btnState
    #BUTTON STATE AT DEFAULT CONDITIONS
    if btnState:
        btn1.config(bg=k, fg=r)
        btn2.config(bg=k, fg=r)
        btn3.config(bg=k, fg=r)
        btn4.config(bg=k, fg=r)
        btn5.config(bg=k, fg=r)
        btn6.config(bg=k, fg=r)
        btn7.config(bg=k, fg=r)
        search_button.config(bg=k,fg=r)
        canvas.config(bg=w)
        labeld.config(bg=w,fg="green")
        txt.config(bg=w,fg=b,font=bladefont)
        playlista.config(bg=w)
        button_frame.config(bg=w)
        r_and_s.config(bg=w)
        labelt.config(bg=w,fg='#b30000',font=myfont)
        scroll.config(bg=w)
        list_box.config(bg=k,fg=g)
        logo_right.config(image=photo_red_right)
        logo_left.config(image=photo_red_left)
        btnState = False
    
    #BUTTON STATE AFTER BEING CLICKED OR BUTTON STATE BECOME TRUE
    else:
        btn1.config(bg=w, fg=r)
        btn2.config(bg=w, fg=r)
        btn3.config(bg=w, fg=r)
        btn4.config(bg=w, fg=r)
        btn5.config(bg=w, fg=r)
        btn6.config(bg=w, fg=r)
        btn7.config(bg=w, fg=r)
        search_button.config(bg=w,fg="red")
        canvas.config(bg=k)
        labeld.config(bg=k,fg=r)
        txt.config( bg=k ,fg=r,font=bladefont)
        button_frame.config(bg=k)
        r_and_s.config(bg=k)
        playlista.config(bg=k)
        labelt.config(bg=k,fg="cyan")
        scroll.config(bg=k)
        list_box.config(bg=k,fg=g)
        logo_right.config(image=photo_blue_right)
        logo_left.config(image=photo_blue_left)
        btnState = True

#TIME
def time():
    string=strftime("%H:%M:%S")
    labelt.config(text=string)
    labelt.after(1000,time)

#VOLUME 
def set_volume(value):
    v=int(value)/100
    pygame.mixer.music.set_volume(v)

#-------------------------------------MAIN-----------------------------------------------

#CANVAS FOR THE PROGRAM TO BE USED 
canvas=tk.Canvas(root,bg=w, height=423,width=562)
canvas.pack()

#IMAGES USED FOR LOGO DARKMODE
photo_blue_left = PhotoImage(file="leftmini.png")
photo_blue_right = PhotoImage(file="rightmini.png")

#IMAGES USED FOR LOGO NORMALMODE

#RIGHT LOGO
photo_red_right = PhotoImage(file="right red xn.png")
logo_right =Label(canvas, image=photo_red_right,bd=0)
logo_right.place(x=327,y=4.5)

#LEFT LOGO
photo_red_left = PhotoImage(file="left red xn.png")
logo_left =Label(canvas, image=photo_red_left,bd=0)
logo_left.place(x=58,y=4.5)


#TITLE
txt=tk.Label(root,text="VIBE CORNER",font=bladefont,fg=b,bg=w)
txt.place(relx=0.25,rely=0.02,relwidth=0.33)

#DARK MODE!!
btn5=tk.Button(canvas,command=switch,bg=k,fg=r,text="DARK MODE",font='FixedSys 5')
btn5.place(relx=0.05,rely=0.83,relwidth=0.2,relheight=0.08)

#VOLUME BUTTON
volume= Scale(canvas, from_=0, to=100, bg=k, showvalue=0, orient=HORIZONTAL, command=set_volume)
volume.set(65)
volume.place(relx=0.35,rely=0.839,relwidth=0.3,relheight=0.07)

#BUTTON_FRAME
button_frame=tk.Frame(root,bd=4,bg=w)
button_frame.place(relheight=0.6,relwidth=0.14,relx=0.75,rely=0.2)

#PLAY__BUTTON
btn2=tk.Button(button_frame,bd=4,bg=k,fg=r,text="Play",font='FixedSys 5',command=play_button)
btn2.place(relx=-0.098,rely=0.2,relwidth=1.2)

#PAUSE__BUTTON
btn3=tk.Button(button_frame,bd=4,text="Pause",bg=k,fg=r,font='FixedSys 5',command=pause_button)
btn3.place(relx=-0.098,rely=0.4,relwidth=1.2)

#NEXT__BUTTON
btn4=tk.Button(button_frame,bd=4,text="Next",bg=k,fg=r,font='FixedSys 5',command=NEXT__SONG)
btn4.place(relx=-0.098,rely=0.6,relwidth=1.2)

#PREVIOUS__BUTTON
btn1=tk.Button(button_frame,bd=4,bg=k,fg=r,text=" Previous",font='FixedSys 5',command=PREVIOUS__SONG)
btn1.place(relx=-0.098,rely=0.035,relwidth=1.2)

#REPEAT--SHUFFLE__FRAME
r_and_s=tk.Frame(root,bd=10,bg=w)
r_and_s.place(relheight=0.301,relwidth=0.11,relx=0.9,rely=0.34)

#REPEAT__BUTTON
btn6=tk.Button(r_and_s,bd=2,text="Repeat",font='Fixedsys 5',bg=k,fg=r,command=repeatbtn)
btn6.place(relx=-0.098,rely=-0.09,relwidth=1.2)

#STOP__BUTTON
btn7=tk.Button(r_and_s,bd=2,text="Stop",font='Fixedsys 5',bg=k,fg=r,command=stop_button)
btn7.place(relx=-0.098,rely=0.312,relwidth=1.2)

#FRAME FOR LIST
playlista=tk.Frame(root,bg=w,bd=10)
playlista.place(relwidth=0.75,relheight=0.6,relx=0.02,rely=0.15)

#LIST_BOX SCROLL_BAR
scroll=Scrollbar(playlista,troughcolor="red")
scroll.pack(side=RIGHT,fill=Y)

#PLAYLIST__BOX
list_box=Listbox(playlista,selectmode=SINGLE,bg=k,fg=g,font=('terminal',14),width=40)
list_box.place(relheight=1,relwidth=0.958)
scroll.config(command=list_box.yview)

#LOAD__BUTTON
search_button=tk.Button(root,bd=3,font='FixedSys 5',text="LOAD",command=browse,fg=r,bg=k)
search_button.place(relx=0.8,rely=0.1015,relheight=0.0694,relwidth=0.15)

#LABEL_FOR_TIME 
labelt=tk.Label(canvas, font=myfont,background=w,foreground=r)
labelt.place(relx=0.7,rely=0.85,relheight=0.0694,relwidth=0.3)
time()

#DAY__DISPLAYING__
today=date.today()

#strn=today.asctime()
labeld=tk.Label(canvas,font='FixedSys 2',text=today,background=w,foreground=g)
labeld.place(relx=0.7,rely=0.9,relheight=0.0694,relwidth=0.3)


#MENU BAR
menu_bar= Menu(root)
root.config(menu=menu_bar)
sub_menu2= Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="About project", command=about)
menu_bar.add_cascade(label="CREDITS", command=credit)


#VOICE__OVER 
engine = pyttsx3.init()
engine.setProperty('rate',100)
x=engine.getProperty('rate')
engine.say("opening vibe corner")
engine.runAndWait()

tk.mainloop()