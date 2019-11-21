from tkinter import *

def affich_1(grille,fenetre,can):
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
    fenetre.mainloop()
    return can

def affich_2(grille_rem,grille_init):
    fenetre=Tk()
    can=Canvas(fenetre,width=500,height=500,bg='white')
    for i in range(4):
        can.create_line(25+i*150,25,25+i*150,475,width=5)
        can.create_line(25,25+i*150,475,25+i*150,width=5)
    for i in range(6):
        can.create_line(75+i*50+(i//2)*50,25,75+i*50+(i//2)*50,475,width=2)
        can.create_line(25,75+i*50+(i//2)*50,475,75+i*50+(i//2)*50,width=2)
    for i in range(9):
        for j in range(9):
            if grille_init[i][j]!=0:
                color="black"
                texte=str(grille_init[i][j])
            else:
                color="blue"
                texte=str(grille_rem[i][j])
            can.create_text(50+j*50,50+i*50,text=texte,font=("Arial","16"),fill=color)
    can.pack()
    fenetre.mainloop()
