from collections import OrderedDict

from more_itertools import strip

def frequence_alphabet(nom_fichier):
    """ 
    Le but de cette fonction est de determiner l'alphabet et la frequence d'appartion des caractères d'un fichier texte

    Args:
    - nom_fichier (str): Le nom du fichier à partir duquel les fréquences de l'alphabet sont extraites.
    """
    # Ouvrir le fichier en mode lecture ('r' signifie lecture)
    with open(nom_fichier, 'r') as file:
        # Lire chaque ligne du fichier dans une liste
        lignes = file.readlines()
        
        i = 0
        alphabet = {}  # Dictionnaire pour stocker les caractères et leur fréquence
        nb_caracteres = 0  # Variable pour compter le nombre total de caractères
        
        # Parcourir chaque ligne du fichier
        while i < len(lignes):
            lignes_en_cours = lignes[i]
            
            # Parcourir chaque caractère de la ligne
            for j in range(len(lignes_en_cours)):
                # Vérifier si le caractère est déjà dans le dictionnaire
                if alphabet.get(f"{lignes_en_cours[j]}") is None:
                    # Si le caractère n'est pas présent, l'ajouter au dictionnaire avec une fréquence de 1
                    alphabet.update({f"{lignes_en_cours[j]}": 1})
                    nb_caracteres += 1
                else:
                    # Si le caractère est déjà présent, augmenter sa fréquence
                    alphabet[f"{lignes_en_cours[j]}"] += 1
            
            i += 1  # Passer à la ligne suivante
        
    # Trier le dictionnaire par clé puis par valeur
    alphabet = OrderedDict(sorted(alphabet.items(), key=lambda t: t[0]))
    alphabet = OrderedDict(sorted(alphabet.items(), key=lambda t: t[1]))
    
    return alphabet,nb_caracteres
    


def creation_fichier_frequence(nom_fichier):
    """
    Cette fonction crée un fichier texte avec l'alphabet et les fréquences de chaque caractère.
    
    Args:
    - nom_fichier (str): Le nom du fichier à partir duquel les fréquences de l'alphabet sont extraites.
    """
    
    # Appeler la fonction frequence_alphabet pour obtenir les fréquences de chaque caractère
    alphabet = frequence_alphabet(nom_fichier)
    
    # Supprimer l'extension du fichier pour obtenir le nouveau nom de fichier
    nom_fichier = nom_fichier[:-4]
    
    # Créer un nouveau fichier avec l'extension "_freq.txt" pour stocker les fréquences
    with open(nom_fichier + "_freq.txt", "w") as fichier:
        # Écrire la fréquence totale dans le fichier
        fichier.write(f"Fréquence totale : {alphabet[1]}\n")
        # Écrire les fréquences de chaque caractère dans le fichier
        for caractere, frequence in alphabet[0].items():
            fichier.write(f"{caractere}: {frequence}\n")





