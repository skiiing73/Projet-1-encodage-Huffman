# Projet-1-encodage-Huffman
Il s'agit du projet 1 du module Projet631 Algorithimique

Le but est de compresser les données par codage de huffman.

Le process utilisé est le suivant :
1. Détermination de l’alphabet et des fréquences de caractères
2. Construction de l’arbre de codage
3. Codage et compression du texte initial
4. le taux de compression obtenu
5. le nombre moyen de bits de stockage d’un caractère dans le texte codé

Pour chacun des textes fournis (<nom>.txt), le programme devra générer un fichier du texte
compressé (<nom>_comp.bin) et un fichier de description de l’alphabet utilisé avec les fréquences
de caractère (<nom>_freq.txt). 
Ces deux fichiers permettront dans le cadre d’un projet de décompression de retrouver le texte initial
dans le mesure où les programmes de compression et de décompression respectent les mêmes règles
de construction de l’arbre de Huffman.


Afin de pouvoir compresser des fichiers il faut que les fichiers tests soient placés dans le dossier fichiers_tests.
Puis dans il faut lancer le programme main.py en prenant soin de modifier la liste des fichiers avec les bons de noms de fichiers que vous souhaitez compresser. 
