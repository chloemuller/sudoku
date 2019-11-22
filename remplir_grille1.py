from tkinter import *
from functools import partial
import time
import numpy
import tkinter as tk
import numpy
from affichage_grille import *

#variable global
grille=numpy.zeros((9,9))
list_case_remplie=[]
color='black'
coord=[-1,-1]
var=0
bien_remplie=False
fenetre=Tk()
can=Canvas(fenetre,width=500,height=500,bg='white')
for i in range(4):
    can.create_line(25+i*150,25,25+i*150,475,width=5)
    can.create_line(25,25+i*150,475,25+i*150,width=5)
for i in range(6):
    can.create_line(75+i*50+(i//2)*50,25,75+i*50+(i//2)*50,475,width=2)
    can.create_line(25,75+i*50+(i//2)*50,475,75+i*50+(i//2)*50,width=2)
can.grid(row=0,column=0,columnspan=10)



def coordonnee(event):
    global var, coord, color,grille, can
    a=int(event.x)
    b=int(event.y)
    if 25<a<475 and 25<b<475 :
        i=(a-25)//50
        j=(b-25)//50
        coord[0]=i
        coord[1]=j
        can.create_rectangle(50+i*50-25,50+j*50-25,50+i*50+25,50+j*50+25,fill="#d4d4d4")
    """else :
        fen = Tk()
        label = Label(fen, text='Hors grille')
        label.pack()
        fen.mainloop()
        coord[0]=-1
        coord[1]=-1"""

def remplir_grille(gril,n):
    global fenetre, can, grille
    if n!=0 :
        grille=numpy.copy(gril)
        for i in range(4):
            can.create_line(25+i*150,25,25+i*150,475,width=5)
            can.create_line(25,25+i*150,475,25+i*150,width=5)
        for i in range(6):
            can.create_line(75+i*50+(i//2)*50,25,75+i*50+(i//2)*50,475,width=2)
            can.create_line(25,75+i*50+(i//2)*50,475,75+i*50+(i//2)*50,width=2)
        for i in range(9):
            for j in range(9):
                if grille[i][j]!=0:
                    color="black"
                    texte=str(int(grille[i][j]))
                else:
                    color="black"
                    texte=' '
                can.create_text(50+j*50,50+i*50,text=texte,font=("Arial","16"),fill=color)
        can.grid(row=0,column=0,columnspan=10)
    #fen,can=init_grille()
    #root=Tk()
    #frame = tk.Frame(fenetre)
    #frame.grid(row=0,column=0,columnspan=10)
    button1 = tk.Button(fenetre,
                   text="1",
                   activebackground = "blue",
                   fg="red",
                   command=var_1)
    #button1.pack(side=tk.LEFT)
    button1.grid(row=1,column=0)
    button2 = tk.Button(fenetre,
                   text="2",
                   activebackground = "blue",
                   fg="red",
                   command=var_2)
    #button2.pack(side=tk.LEFT)
    button2.grid(row=1,column=1)
    button3 = tk.Button(fenetre,
                   text="3",
                   activebackground = "blue",
                   fg="red",
                   command=var_3)
    #button3.pack(side=tk.LEFT)
    button3.grid(row=1,column=2)
    button4 = tk.Button(fenetre,
                   text="4",
                   activebackground = "blue",
                   fg="red",
                   command=var_4)
    #button4.pack(side=tk.LEFT)
    button4.grid(row=1,column=3)
    button5 = tk.Button(fenetre,
                   text="5",
                   activebackground = "blue",
                   fg="red",
                   command=var_5)
    #button5.pack(side=tk.LEFT)
    button5.grid(row=1,column=4)
    button6 = tk.Button(fenetre,
                   text="6",
                   activebackground = "blue",
                   fg="red",
                   command=var_6)
    #button6.pack(side=tk.LEFT)
    button6.grid(row=1,column=5)
    button7 = tk.Button(fenetre,
                   text="7",
                   activebackground = "blue",
                   fg="red",
                   command=var_7)
    #button7.pack(side=tk.LEFT)
    button7.grid(row=1,column=6)
    button8 = tk.Button(fenetre,
                   text="8",
                   activebackground = "blue",
                   fg="red",
                   command=var_8)
    #button8.pack(side=tk.LEFT)
    button8.grid(row=1,column=7)
    button9 = tk.Button(fenetre,
                   text="9",
                   activebackground = "blue",
                   fg="red",
                   command=var_9)
    #button9.pack(side=tk.LEFT)
    button9.grid(row=1,column=8)
    button0 = tk.Button(fenetre,
                   text="  ",
                   activebackground = "blue",
                   fg="red",
                   command=var_)
    #button0.pack(side=tk.LEFT)
    button0.grid(row=1,column=9)
    button=tk.Button(fenetre,
                   text="grille remplie",
                   activebackground = "blue",
                   fg="red",
                   command=remplie)
    button.grid(row=2,column=4,columnspan=2)
    fenetre.bind("<Button-1>",coordonnee)
    #can.pack()
    #funt = lambda v,i,j : (can.create_text(50+i*50,50+j*50,text=v,font=("Arial","16"),fill=color),grille[i][j]=int(v),can.pack())
    #funt(str(var),coord[0],coord[1])
    #can.pack()
    fenetre.mainloop()
    #root.mainloop()
    return grille

def var_1():
    global coord, can, color
    i=coord[0]
    j=coord[1]
    grille[j][i]=1
    can.delete("all")
    affich_1(grille,fenetre,can)

def var_2():
    global coord, can, color
    i=coord[0]
    j=coord[1]
    grille[j][i]=2
    can.delete("all")
    affich_1(grille,fenetre,can)


def var_3():
    global coord, can
    i=coord[0]
    j=coord[1]
    grille[j][i]=3
    can.delete("all")
    affich_1(grille,fenetre,can)

def var_4():
    global coord, can
    i=coord[0]
    j=coord[1]
    grille[j][i]=4
    can.delete("all")
    affich_1(grille,fenetre,can)

def var_5():
    global coord, can
    i=coord[0]
    j=coord[1]
    grille[j][i]=5
    can.delete("all")
    affich_1(grille,fenetre,can)

def var_6():
    global coord, can
    i=coord[0]
    j=coord[1]
    grille[j][i]=6
    can.delete("all")
    affich_1(grille,fenetre,can)

def var_7():
    global coord, can
    i=coord[0]
    j=coord[1]
    grille[j][i]=7
    can.delete("all")
    affich_1(grille,fenetre,can)

def var_8():
    global coord, can, list_case_remplie
    i=coord[0]
    j=coord[1]
    grille[j][i]=8
    can.delete("all")
    affich_1(grille,fenetre,can)


def var_9():
    global coord, can, list_case_remplie
    i=coord[0]
    j=coord[1]
    grille[j][i]=9
    can.delete("all")
    affich_1(grille,fenetre,can)

def var_():
    global coord, can
    i=coord[0]
    j=coord[1]
    grille[j][i]=0
    can.delete("all")
    affich_1(grille,fenetre,can)

def remplie():
    fenetre.destroy()
    return grille

def traiter_grille(gril):
    global fenetre,can,grille
    grille=numpy.copy(gril)
    for i in range(4):
        can.create_line(25+i*150,25,25+i*150,475,width=5)
        can.create_line(25,25+i*150,475,25+i*150,width=5)
    for i in range(6):
        can.create_line(75+i*50+(i//2)*50,25,75+i*50+(i//2)*50,475,width=2)
        can.create_line(25,75+i*50+(i//2)*50,475,75+i*50+(i//2)*50,width=2)
        for i in range(9):
            for j in range(9):
                if grille[i][j]!=0:
                    color="black"
                    texte=str(int(grille[i][j]))
                else:
                    color="black"
                    texte=' '
                can.create_text(50+j*50,50+i*50,text=texte,font=("Arial","16"),fill=color)
    can.grid(row=0,column=0,columnspan=10)
    button1 = tk.Button(fenetre,
                   text="Valider la grille",
                   activebackground = "blue",
                   fg="red",
                   command=resoud_grille_valide)
    #button1.pack(side=tk.LEFT)
    button1.grid(row=1,column=0,columnspan=3)
    button2 = tk.Button(fenetre,
                   text="Corriger la grille",
                   activebackground = "blue",
                   fg="red",
                   command=corriger_grille)
    #button2.pack(side=tk.LEFT)
    button2.grid(row=1,column=3,columnspan=3)
    button3 = tk.Button(fenetre,
                   text="Remplir la grille",
                   activebackground = "blue",
                   fg="red",
                   command=remplir_la_grille)
    #button3.pack(side=tk.LEFT)
    button3.grid(row=1,column=6,columnspan=3)
    fenetre.mainloop()
    return grille

def resoud_grille_valide () :
    return grille

def corriger_grille ():
    global grille
    grid=remplir_grille(grille,1)
    grille=numpy.copy(grid)

def remplir_la_grille ():
    global grille
    grid=remplir_grille(grille,0)
    grille=numpy.copy(grid)

