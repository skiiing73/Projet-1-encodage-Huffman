from frequence_caractere import *
from Arbre_binaire import * 
from encodage_caractere import *
nomfichier="textesimple.txt"
# creation du fichier de frequence 
creation_fichier_frequence(nomfichier)
# Création de l'arbre de Huffman et affichage
huffman_tree = creerArbre(nomfichier)
#creation d'un dictionnaire contenant le code des caracteres
dict_encode=encodage_caractere(huffman_tree)
print(dict_encode)
#creation du fichier binaire
encodage_fichier(nomfichier,dict_encode)