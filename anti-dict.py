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
            # Si i n'est pas dans common words
            # appliquer la troncature et ecrire dans le fichier f
            if (not (i in cw)):
                f.write(stemmer.stem(i.lower())+" ")
        f.close()

antidict(inputDirectory)