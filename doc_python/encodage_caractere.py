from Arbre_binaire import *
from bitarray import bitarray

def encodage_caractere(huffman_tree):
    """
    Encode les caractères de l'arbre de Huffman.
    Parameters:
    huffman_tree : L'arbre de Huffman à encoder
    Returns:
    dict: dictionnaire contenant les caractères et leurs codes correspondants.
    """
    dict={}
    def rec_encodage_caractere(node,dict,encodage):
        """
        Fonction récursive pour parcourir l'arbre et encoder les caractères.
        Parameters:
        node (Node): Le nœud actuel à explorer.
        dict (dict): Dictionnaire de codage pour stocker les caractères et leurs codes.
        encodage (str): l'encodage du caractere en cours.
        """

        if node.getleftChild() is None and node.getrightChild() is None:
            dict[node.getcaractere()]=encodage
        else:

            if node.getleftChild()!=None:
                rec_encodage_caractere(node.getleftChild(),dict,encodage+"0")
            if node.getrightChild()!=None:
                rec_encodage_caractere(node.getrightChild(),dict,encodage+"1")
       
    rec_encodage_caractere(huffman_tree.getroot(),dict,"")
    
    return dict

def encodage_fichier(nomfichier,dict):
    """
    Encode le contenu d'un fichier en utilisant un dictionnaire de codage pour compresser les données.
    
    Args:
    - nomfichier (str): Le nom du fichier à encoder.
    - dict (dict): Le dictionnaire de codage contenant les caractères et leurs codes correspondants.
    """
    
    res=bitarray()
    with open(nomfichier, 'r') as file:
        # Lire chaque ligne du fichier dans une liste
        lignes = file.readlines()
        # Parcourir chaque ligne du fichier
        for ligne in lignes:
            # Parcourir chaque caractère de la ligne
            for caractere in ligne:
                # Ajouter le code du caractère correspondant à la séquence de bits
                res.extend(dict[caractere])

    nom_fichier_ecriture = nomfichier[:-4] + "_comp.bin"
    with open(nom_fichier_ecriture, "wb") as fichier:
        # Écrire la fréquence totale dans le fichier
        res.tofile(fichier)

    