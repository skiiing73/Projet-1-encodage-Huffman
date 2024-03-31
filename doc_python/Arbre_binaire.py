from frequence_caractere import *

class Node:
    """
    Classe Node
    La classe représente un nœud d'un arbre binaire.
    """
    def __init__(self, caractere, frequence, leftChild=None, rightChild=None):
        # Initialisation des attributs du nœud
        self.frequence = frequence
        self.caractere = caractere
        self.leftChild = leftChild
        self.rightChild = rightChild

    # Méthodes pour obtenir des informations sur le nœud
    def getleftChild(self):
        return self.leftChild

    def getrightChild(self):
        return self.rightChild

    def getcaractere(self):
        return self.caractere

    def getfrequence(self):
        return self.frequence

    # Méthodes pour définir les enfants du nœud
    def setrightChild(self, node):
        self.rightChild = node

    def setleftChild(self, node):
        self.leftChild = node

    def setcaractere(self,new_value):
        self.caractere=new_value
    # Méthode d'affichage du nœud
    def __str__(self):
        return f"{self.caractere}:{self.frequence}"
    def is_leaf(self):
        if self.leftChild is self.rightChild is None:
            return True
        return False

class Tree:
    """
    Classe Tree
    Cette classe représente un arbre binaire par sa racine.
    """
    def __init__(self, root):
        # Initialisation de l'arbre avec sa racine
        self.root = root

    # Méthode pour obtenir la racine de l'arbre
    def getroot(self):
        return self.root

    # Méthode pour définir la racine de l'arbre
    def setroot(self, node):
        self.root = node

    # Méthode d'affichage de l'arbre
    def __str__(self):
        return self.print_tree(self.root, 0)

    # Méthode récursive pour l'affichage de l'arbre 
    def print_tree(self, node, indent, is_right=False):
         if node is None:
             return ""
         result = ""
         if node.getrightChild():
             result += self.print_tree(node.getrightChild(), indent + 4, True)
         result += " " * indent
         if is_right:
             result += " /"
         else:
             result += " \\"
         result += f"__{str(node)}\n"
         if node.getleftChild():
             result += self.print_tree(node.getleftChild(), indent + 4, False)
         return result
    

        

def minArbre(liste):
    """
    Cette fonction retourne l'arbre de fréquence minimale d'une liste d'arbres.

    Returns:
    Tree
    """
    min_arbre = liste[0]
    for el in liste:
        if el.getroot().getfrequence() < min_arbre.getroot().getfrequence():
            min_arbre = el
    return min_arbre

def creerArbre(nomfichier,action=None):
    """
    Cette fonction crée un arbre de Huffman à partir d'une liste de fréquences d'un texte.

    Returns:
    Tree
    """
    
    # Obtention des fréquences de chaque caractère dans le texte
    if action=="decodage":
        alphabet=frequence_alphabet_decodage(nomfichier)
       
    else:
        alphabet = frequence_alphabet_encodage(nomfichier)
        
    liste_arbres = []
    # Création d'un arbre pour chaque caractère
    for el in alphabet[0].keys():
        noeud = Node(el, alphabet[0][el])
        arbre = Tree(noeud)
        liste_arbres.append(arbre)

    # Construction de l'arbre de Huffman
    while len(liste_arbres) > 1:
        t1 = minArbre(liste_arbres)
        liste_arbres.remove(t1)
        t2 = minArbre(liste_arbres)
        liste_arbres.remove(t2)
    
        # Création d'un nouveau nœud interne avec les arbres t1 et t2 comme enfants
        noeud_t = Node("intermediaire", t1.getroot().getfrequence() + t2.getroot().getfrequence(), t1.getroot(), t2.getroot())
        arbret = Tree(noeud_t)
        liste_arbres.insert(0, arbret)
    
    return liste_arbres[0]


