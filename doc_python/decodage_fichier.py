from encodage_fichier import *
def inverser_compression(nomfichier):
    """
    Permet de reconvertir les données binaires du fichier en chaînes de caractères de 0 et 1 correspondant à l'encodage des caractères.
    Cette fonction permet seulement de vérifier que la conversion des données en binaire a bien été effectuée.
    
    Args:
    nomfichier (str): Nom du fichier binaire.
    """
    res = ""
    with open(nomfichier, 'rb') as file:
        # Lire toutes les données binaires du fichier
        donnees_binaires = file.read()
        # Convertir les données binaires en une chaîne binaire de '0' et '1'
        res = ''.join(format(byte, '08b') for byte in donnees_binaires)
    
    return res

def decodage_fichier(nomfichier,huffmantree):
    """
    Permet  de décoder un  fichier a partir du fichier binaire et de l'arbre de huffman qui lui est associé
    
    Parameters:
    nomfichier (str): Nom du fichier binaire.
    huffman tree (Tree): arbre de huffman associé au fichier 
    Return:
    listes des caracteres du fichier décompressé
    """
    chaines_encodee=inverser_compression(nomfichier)
    res=[]
    if len(chaines_encodee) < 1000:
        # Si le fichier est assez petit, on utilise le parcours de l'arbre pour chaque caractere
        def rec_decodage_fichier(node, chaines_encodees, res, huffmantree):
            if chaines_encodees == "" or len(res)==huffmantree.getroot().getfrequence():
                return res
            elif node.getleftChild() is None and node.getrightChild() is None:
                # Si le nœud est une feuille, ajoute le caractère au résultat
                res.append(node.getcaractere())
                # Recherche à partir de la racine pour le prochain caractère
                rec_decodage_fichier(huffmantree.getroot(), chaines_encodees, res, huffmantree)
            else:
                if chaines_encodees[0] == "0":
                    newchaines_encodees = chaines_encodees[1:]
                    rec_decodage_fichier(node.getleftChild(), newchaines_encodees, res, huffmantree)
                elif chaines_encodees[0] == "1":
                    newchaines_encodees = chaines_encodees[1:]
                    rec_decodage_fichier(node.getrightChild(), newchaines_encodees, res, huffmantree)

        rec_decodage_fichier(huffmantree.getroot(), chaines_encodee, res, huffmantree)
    else:
        # Si le fichier est trop gros, la méthode de l'arbre n'est pas adaptée
        # On procède donc autrement
        
        dict_encode = encodage_caractere(huffmantree)
        res_tempo = ""#liste temporaire permettant de stocker la valeur d'encodage du caractere jusqu'a ce qu'il soit décoder
        for i in range(len(chaines_encodee)):
            res_tempo += chaines_encodee[i]
            if res_tempo in dict_encode.values():
                # Si la séquence encodée correspond à une valeur dans le dictionnaire, ajoute la clé au résultat
                for key, value in dict_encode.items():
                    if value == res_tempo:
                        res.append(key)
                        res_tempo = ""#on reinitialise la liste tempo car la chaine de bits a trouvé un caractère 
    return res
