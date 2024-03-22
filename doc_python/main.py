from frequence_caractere import *
from Arbre_binaire import * 
from encodage_caractere import *
from bitarray import bitarray
import os


liste_fichiers=["textesimple.txt","extraitalice.txt","alice.txt"]
def compression(nomfichier):
    """
    cette fonction permet de compresser un fichier texte en un fichier binaire qui est créé
    
    Args:nomfichier (str)
    
    """
    # creation du fichier de frequence 
    creation_fichier_frequence(nomfichier)
    # Création de l'arbre de Huffman et affichage
    huffman_tree = creerArbre(nomfichier)
    #creation d'un dictionnaire contenant le code des caracteres
    dict_encode=encodage_caractere(huffman_tree)
    def nb_moyenbits(dict):
        """
        Calcul du nombre moyen de bits par caractere
        
        Args: 
        dictionnaire avec les caracteres et leur encodage
        
        Return:
        nb de bits moyen
        """
        res=0
        cpt=0
        for encodage in dict.items():
            res+=len(encodage)
            cpt+=1
        return res/cpt
    bits_moyen=nb_moyenbits(dict_encode)
    #creation du fichier binaire
    encodage_fichier(nomfichier,dict_encode)
    print("fichier: ",nomfichier," compressé avec succès.\n Le nombre moyen de bits par caractère est de ",bits_moyen," bits.")


def taux_compression(file_txt,file_bin):
    """
    Calcul le taux de compression d'un fichier
    
    Args:
    file_txt(str) qui est le nom du fichier texte
    file_bin(str) qui est le nom du fichier binaire
    
    """
    sizefile_txt=os.path.getsize(file_txt)
    sizefile_bin=os.path.getsize(file_bin)
    print("taux de compression du fichier: ",round(1-(sizefile_bin/sizefile_txt),4))
    

def inverser_compression(nomfichier):
    """
    permet de reconvertir les données binaire du fichier en chaines de caracteres de 0 et 1 correspondant a l'encodage des caractères
    Cette fonction permet seulement de verifier que la conversion des données en binaire a bien été effectué
    
    Args:
    nomfichier (str) nom du fichier binaire """
    with open(nomfichier, 'rb') as file:
            # Lire chaque ligne du fichier dans une liste
           
            lignes = file.readlines()
            # Parcourir chaque ligne du fichier
            for ligne in lignes:
                donnees_binaires=ligne
                donnees_str = ''.join(format(byte, '08b') for byte in donnees_binaires)
                print(donnees_str)

if __name__ =="__main__":
    #compression et affichage des statistiques des fichiers de données
    for fichier in liste_fichiers:
        compression(fichier)
        fichierbinaire=fichier[:-4]+ "_comp.bin"
        taux_compression(fichier,fichierbinaire)