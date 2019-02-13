import os
from nltk.stem.porter import *

inputDirectory = "../clean/"
outputDirectory = "../antiDict/"

def antidict(indir):
    cwfh = open("../common_words", "r")
    cw = cwfh.read().split("\n")
    cwfh.close()

    stemmer = PorterStemmer() # creation d'un objet stemmer
    for file in os.listdir(indir):
        wordsfh = open(indir+file, "r")
        words = wordsfh.read().split(" ")
        wordsfh.close()
        f = open(outputDirectory+file.strip(".flt")+".sttr", "w+")
        for i in words:
            if (not (i in cw)):
                f.write(stemmer.stem(i.lower())+" ")
        f.close()

antidict(inputDirectory)