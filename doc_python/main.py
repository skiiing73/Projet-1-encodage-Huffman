from frequence_caractere import *
from Arbre_binaire import * 
from encodage_fichier import *
from decodage_fichier import *
from bitarray import bitarray
import os

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
            res+=len(encodage[1])
            cpt+=1
        return round(res/cpt,4)
    
    bits_moyen=nb_moyenbits(dict_encode)
    #creation du fichier binaire
    encodage_fichier(nomfichier,dict_encode)
    print("fichier: ",nomfichier," compressé avec succès.\nLe nombre moyen de bits par caractère est de ",bits_moyen," bits.")


def taux_compression(file_txt,file_bin):
    """
    Calcul le taux de compression d'un fichier
    
    Args:
    file_txt(str) qui est le nom du fichier texte
    file_bin(str) qui est le nom du fichier binaire
    
    """
    sizefile_txt=os.path.getsize(file_txt)
    sizefile_bin=os.path.getsize(file_bin)
    print("Taux de compression du fichier: ",round(1-(sizefile_bin/sizefile_txt),4))
    

def decompression(nomfichierbin,nomfichier_freq):
     # Création de l'arbre de Huffman et affichage
    huffman_tree = creerArbre(nomfichier_freq,"decodage")
    res=decodage_fichier(nomfichierbin,huffman_tree)
    
    nomfichier=nom_fichier = nomfichier_freq[:-9]+"_decode.txt"
    with open(nomfichier , "w") as fichier:
        # Écrire la fréquence totale dans le fichier
        for el in res:
            fichier.write(el)
    print("décodage du fichier "+nomfichier_freq[:-9]+ " terminé.")


if __name__ =="__main__":
    
    liste_fichiers_a_encoder=["fichiers_tests_encodage/textesimple.txt","fichiers_tests_encodage/extraitalice.txt","fichiers_tests_encodage/alice.txt"]
    
    #compression et affichage des statistiques des fichiers de données
    for fichier in liste_fichiers_a_encoder:
        compression(fichier)
        fichierbinaire=fichier[:-4]+ "_comp.bin"
        taux_compression(fichier,fichierbinaire)

    #ecrire le nom correct des fichiers en rentrant en premier le fichier binaire puis l'alphabet dans une sous-liste 
    liste_fichiers_a_decoder=[["fichiers_tests_decodage/exemple_comp.bin","fichiers_tests_decodage/exemple_freq.txt"],["fichiers_tests_encodage/textesimple_comp.bin","fichiers_tests_encodage/textesimple_freq.txt"]]
    for fichier in liste_fichiers_a_decoder:
        decompression(fichier[0],fichier[1])
    
    
  