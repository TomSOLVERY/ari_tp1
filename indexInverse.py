import json
import os

inputDirectory = "../json/"

def indexInvers(indir, outdir):
    # chargement du vocabulaire
    vocabfh = open(indir+"vocabulaire.json", "r")
    vocab = json.load(vocabfh)
    vocabfh.close()
    # chargement des vecteurs de docs
    vectfh = open(indir+"vect.json", "r")
    vect = json.load(vectfh)
    vectfh.close()
    # Le dictionnaire resultat
    res = {}
    for terme in vocab:
        # dictionnaire idDoc: idf du terme dans le doc
        tfidf = {}
        for idDoc in vect:
            if terme in vect[idDoc]:
                tfidf[idDoc] = vect[idDoc][terme]
        res[terme] = tfidf
    # ecriture du resultat
    f = open(outdir+"indexInverse.json", "w+")
    json.dump(res, f)
    f.close()

indexInvers(inputDirectory, inputDirectory)