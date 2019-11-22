import cv2
from pylab import imread, imshow, show
from numpy import array, zeros
from keras.models import load_model
from image_to_bin import pngToGrey, greyToBin
from contours import get_clean_grid


def decoupage(nom_image, grey = True):
    im = cv2.imread(nom_image)
    im = get_clean_grid(im)
    imshow(im)
    show()
    if grey :
        grey = pngToGrey(im)
        im = greyToBin(grey)
    #on va découper la grille en 81 cases
    size = len(im)
    cell_size = size//9 #en pixels
    cells = []
    for row in range(9):
        for column in range(9):
            cells.append(extract_cell(row, column, im, cell_size, grey))
    return cells


def extract_cell(row, column, image, cell_size, grey = True):
    left_boundary = row*cell_size
    right_boundary = (row+1)*cell_size
    up_boundary = column*cell_size
    down_boundary = (column+1)*cell_size
    if grey :
        cell = array([[0 for i in range(cell_size)] for j in range(cell_size)])
    else :
        cell = array([[[float(0) for c in range(image.shape[2])]for i in range(cell_size)] for j in range(cell_size)])
    for i in range(left_boundary, right_boundary):
        for j in range(up_boundary, down_boundary):
            iprime = i-left_boundary    #les indices primes representent les indices de la cellule
            jprime = j-up_boundary      #les indices non primes representent les indices de l'image
            if grey :
                cell[iprime][jprime] = image[i][j]
            else :
                for c in range(image.shape[2]):
                    cell[iprime][jprime][c] = image[i][j][c]
    return cell



def extract_amas(cell):
    size_cell = len(cell)
    carte = [[-1 for i in range(size_cell)] for j in range(size_cell)]
    milieu = size_cell//2
    front = [(milieu, milieu)]
    carte[milieu][milieu] = 1
    while not noir_in_front(front, cell)[0]:
        front, carte = front_superieure(front, carte, cell)
    pixels_noirs = noir_in_front(front, cell)[1]
    amas = pixels_noirs
    amas = grossir_amas(cell, amas, carte)
    return amas


def grossir_amas(cell, amas, carte):
    # print(cell)
    # print(cell.shape)
    amas_a_grossi = True 
    while amas_a_grossi :
        amas_a_grossi = False
        for pixel in amas :
            for voisin in pixels_voisins(pixel):
                i, j = voisin
                if i < len(cell) and j < len(cell) :
                    if carte[i][j] == -1 :
                        if cell[i][j] == 0:
                            amas.append((i,j))
                            amas_a_grossi = True
                            carte[i][j] = 0
                        else :
                            carte[i][j] = 1
    return amas


def noir_in_front(front, cell):
    pixels_noirs = []
    for pixel in front :
        i, j = pixel
        if cell[i][j] == 0 :
            pixels_noirs.append(pixel)
    if pixels_noirs != [] :
        return True, pixels_noirs
    else :
        return False, []


def front_superieure(front, carte, cell):
    nouvelle_front = []
    for pixel in front :
        for voisin in pixels_voisins(pixel):
            i, j = voisin
            if carte[i][j] == -1 :
                nouvelle_front.append(voisin)
                if cell[i][j] == 1 :
                    carte[i][j] = 1
                else :
                    carte[i][j] = 0
    return nouvelle_front, carte


def pixels_voisins(pixel):
    i, j = pixel
    return [(i+1, j), (i, j+1), (i-1, j), (i, j-1)]


def amas_to_28pixels(amas):
    print("amas", amas)
    #On centre d'abord le nombre extrait dans le premier 
    hauteur = max([pixel[0] for pixel in amas]) - min([pixel[0] for pixel in amas])
    largeur = max([pixel[1] for pixel in amas]) - min([pixel[1] for pixel in amas])
    espace_vide_gauche = min([pixel[0] for pixel in amas])
    espace_vide_haut = min([pixel[1] for pixel in amas])
    surplus = abs(hauteur-largeur)//2
    border = int(max(hauteur, largeur)*0.2) + 1  # le + 1 est pour dans le cas ou l'amas a une taille de 1 (rare mais pas impossible)
    if hauteur > largeur :
        number_size = hauteur  #la taille du nombre dans un carré
        decallage_horizontal = espace_vide_gauche - border//2
        decallage_vertical = espace_vide_haut - surplus - border//2
    else :
        number_size = largeur
        decallage_horizontal = espace_vide_gauche - surplus - border//2
        decallage_vertical = espace_vide_haut - border//2
    cell_size = number_size + border
    image = array([[0 for i in range(cell_size)] for j in range(cell_size)])
    for i in range(cell_size):
        for j in range(cell_size):
            if (i + decallage_horizontal, j + decallage_vertical) in amas :
                image[i][j] = 1
    print("image", image)
    cv2_image = convert_bitmap_to_cv2(image)
    print(cv2_image)
    print(cv2_image.shape)
    cv2_resized_image = cv2.resize(cv2_image, (28,28))
    resized_image = convert_cv2_to_bitmap(cv2_resized_image)
    return resized_image


def convert_bitmap_to_cv2(bitmap_image):
    cv2_image = zeros(list(bitmap_image.shape) + [3])
    for i in range(bitmap_image.shape[0]):
        for j in range(bitmap_image.shape[1]):
            if bitmap_image[i][j] == 0 :
                for c in range(3):
                    cv2_image[i][j][c] = 0
            else :
                for c in range(3):
                    cv2_image[i][j][c] = 255
    return cv2_image


def convert_cv2_to_bitmap(cv2_image):
    bitmap_image = zeros(list(cv2_image.shape[:2]))
    for i in range(cv2_image.shape[0]):
        for j in range(cv2_image.shape[1]):
            if cv2_image[i][j][0] == 255 :
                bitmap_image[i][j] = 1
            else :
                bitmap_image[i][j] = 0
    return bitmap_image

            
def interpret(outputs):
    results = []
    for output in outputs :
        maximum = max(output)
        results.append(list(output).index(maximum))
    return results


def prediction(images):
    images = images.reshape(images.shape[0], 28, 28, 1).astype('float32')
    model = load_model('CNN')
    outputs = model.predict(images)
    return interpret(outputs)


def picture_to_grid(nom_image):
    cells = decoupage(nom_image)
    cells_couleur = decoupage(nom_image, grey = False)
    blank = []
    images = []
    for i in range(len(cells)):
        amas = extract_amas(cells[i])
        blank.append(detect_blank_cells(amas, cells_couleur[i]))
        if not blank[i] :
            images.append(amas_to_28pixels(amas))
    results = prediction(array(images))
    grid = array([[0 for i in range(9)] for j in range(9)])
    count_blank = 0
    count_all = 0   #cette variable numérote les cases pleines
    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            if not blank[count_all] :
                grid[i][j] = results[count_blank]
                count_blank += 1
            count_all += 1
    return grid



def detect_blank_cells(amas, cell_couleur):
    # on fait la moyenne des couleurs des pixels de l'amas
    somme = 0 
    for pixel in amas :
        i, j = pixel
        for c in range(cell_couleur.shape[2]):
            somme += cell_couleur[i][j][c]/3
    moyenne_amas = somme/len(amas)
    somme = 0 
    for i in range(cell_couleur.shape[0]):
        for j in range(cell_couleur.shape[1]):
            for c in range(cell_couleur.shape[2]):
                somme += cell_couleur[i][j][c]/3
    moyenne_cell = somme/(cell_couleur.shape[0]*cell_couleur.shape[1])
    #if case remplie
    if moyenne_cell - 0.08  > moyenne_amas :    # On rajoute le -0.08 car parfois dans une case vide la couleur de l'amas est très légèrement inférieure à la couleur moyenne
        return False
    #if case vide
    else :
        return True



print(picture_to_grid("sudoku_original.png"))

    
