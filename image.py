# img : fichier array avec 0=blanc 1=noir
img_test= [[0,0,0,1],[0,1,0,1],[1,1,0,0],[0,1,0,0]]

def coordonnees_voisines(liste_points):
    voisins=[]
    for (x,y) in liste_points:
        for (i,j) in [(x+1,y),(x,y-1),(x-1,y),(x,y+1)]:
            if (i,j) not in voisins and (i,j) not in liste_points:
                voisins.append((i,j))
    return voisins

def couleur(liste, img):
    couleurs=[]
    for (i,j) in liste:
        couleurs.append(img[i][j])
    return couleurs

def amas_pixels_blancs(img):
    amas=[]
    pixels=[(i,j) for i in range(len(img)) for j in range(len(img[0]))]
    pixels_explores=[]
    while len(pixels_explores)!=len(pixels) :
        for pixel in pixels:
            if pixel not in pixels_explores:
                x=pixel[0]
                y=pixel[1]
                print("pixel_courant",pixel)
                if img[x][y]==1:
                    pixels_explores.append((x,y))
                else:
                    amas1=[] 
                    amas1.append((x,y))
                    pixels_explores.append((x,y))
                    front=[(x,y)]
                    while front!=[]:
                        for (i,j) in front:
                            if (i,j) not in pixels_explores and (i,j) in pixels:
                                if img[i][j]==0:
                                    amas1.append((i,j))
                                    pixels_explores.append((i,j))
                            voisins=coordonnees_voisines(front)
                            front2=[]
                            for couple in voisins:
                                (a,b)=couple
                                if couple not in pixels_explores and couple in pixels and img[a][b]==0:
                                    front2.append(couple)
                            front=front2.copy()
                        print("frontiere", front, front!=[])
                    amas.append(amas1)
    return amas



print(amas_pixels_blancs(img_test))
