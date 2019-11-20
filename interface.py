from tkinter import *
from tkinter.filedialog import *

image=""

def recherche_fichiers():
    image = askopenfilename(filetypes=[("PNG","*.png")], title="Choisissez votre fichier")

def tk_interface():
    window=Tk()
    window.title("Sudoku Resolver")
    label = Label(window, text="Rentrez ici votre image de sudoku à résoudre :")
    label.pack()

    #choix1=Radiobutton (window, variable=IntVar(), text="Je souhaite télécharger ma photo", value=1, command=recherche_fichiers(window))
    #choix2=Radiobutton (window, variable=IntVar(), text="Je souhaite prendre une photo avec la webcam", value=1)

    bouton_choix1 = Button(window, text="Je souhaite télécharger ma photo", activebackground="red", command=recherche_fichiers)
    bouton_choix2 = Button(window, text="Je souhaite prendre une photo avec la webcam", command=window.quit)
    bouton_choix1.pack()
    bouton_choix2.pack()

    window.mainloop()
    print(image)

tk_interface()