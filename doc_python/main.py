from frequence_caractere import *
from Arbre_binaire import * 

nomfichier="textesimple.txt"
# creation du fichier de frequence 
creation_fichier_frequence(nomfichier)
# Création de l'arbre de Huffman et affichage
huffman_tree = creerArbre(nomfichier)

