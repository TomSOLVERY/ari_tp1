# 4 - anti-dict.py
# Fonction qui applique l'anti-dictionnaire (fichier common-words)
# sur les mots en minuscule en enlevant tous les termes de ces fichiers qui y apparaissent. 
# Le resultat du filtrage est mis dans un fichier portant le meme nom que ces fichiers avec 
# une nouvelle extension .sttr 

import os
from nltk.stem.porter import *

inputDirectory = "../clean/"
outputDirectory = "../antiDict/"

def antidict(indir):
    # chargement de l'anti-dictionnaire
    cwfh = open("../common_words", "r")
    cw = cwfh.read().split("\n")
    cwfh.close()

    stemmer = PorterStemmer() # creation d'un objet stemmer
    for file in os.listdir(indir):
        # chargement des mots du fichier
        wordsfh = open(indir+file, "r")
        words = wordsfh.read().split(" ")
        wordsfh.close()

        f = open(outputDirectory+file.strip(".flt")+".sttr", "w+")
        for i in words:
            # Si i en minuscule n'est pas dans common words
            # appliquer la troncature et ecrire dans le fichier f
            if (not (i.lower() in cw)):
                f.write(stemmer.stem(i.lower())+" ")
        f.close()

antidict(inputDirectory)