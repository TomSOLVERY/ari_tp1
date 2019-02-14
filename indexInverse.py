import json
import os

inputDirectory = "../json/"

def indexInvers(indir):
    # chargement du vocabulaire
    vocabfh = open(indir+"vocabulaire.json", "r")
    vocab = json.load(vocabfh)
    vocabfh.close()
    # chargement des vecteurs de docs
    vectfh = open(indir+"vect.json", "r")
    vect = json.load(vectfh)
    vectfh.close()


    

indexInvers(inputDirectory)