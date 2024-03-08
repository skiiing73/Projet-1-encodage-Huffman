from frequence_caractere import frequence_alphabet


class Node:
    """
    Classe Node
    La classe prend en paramètres le nom du nœud et son fils droit et son fils gauche.
    """
    def __init__(self, values, leftChild=None, rightChild=None):
        self.values = values
        self.leftChild = leftChild
        self.rightChild = rightChild

    def getleftChild(self):
        return self.leftChild
    
    def getrightChild(self):
        return self.rightChild
    
    def getcaractere(self):
        return self.values
    
    def setrightChild(self, node):
        self.rightChild = node

    def setleftChild(self, node):
        self.leftChild = node


class Tree:
    """
    Classe Tree 
    Cette classe représente un arbre binaire par sa racine.
    """
    def __init__(self, root):
        self.root = root

    def getroot(self):
        return self.root
    
    def setroot(self, node):
        self.root = node

def creerArbre():
    alphabet = frequence_alphabet("textesimple.txt")
    liste_arbres = []
    
    for el in alphabet[0].keys():
        nom_noeud = "noeud" + el
        noeud = Node(el)
        
        nom_arbre = "arbre" + el
        arbre = Tree(noeud)
        
        liste_arbres.append(arbre)
    
    print(liste_arbres)

creerArbre()
