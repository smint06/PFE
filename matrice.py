mat = []        #création d'une liste vide
with open ("E:/synthetic_control.data","r") as f :      #ouverture du fichier en mode lecture
    for li in f :       #pour toutes les lignes du fichier :
        s=li.strip('\n\r')      # on enlève les caractère de fin de ligne
        l = s.split(" ")        # on découpe en colonnes
        mat.append(l)           # on ajoute la ligne à la matrice
print(mat)      #affichage de la matrice