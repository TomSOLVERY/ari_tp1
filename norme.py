# 8 - norme.py
# calcul de le norme de chaque document

import json
from math import sqrt

inputDirectory = "../json/"

def norme (indir, outdir):
    # chargement des vecteurs de docs
    vectfh = open(indir+"vect.json", "r")
    vect = json.load(vectfh)
    vectfh.close()
    # dictionnaire resultat
    res = {}
    # calcul de la norme
    for idDoc in vect:
        norm = 0
        for terme in vect[idDoc]:
            norm = norm + (vect[idDoc][terme]*vect[idDoc][terme])
        res[idDoc] = sqrt(norm)
    # verification du resultat
    f = open(outdir+"norm.json", "w+")
    json.dump(res, f)
    f.close()

norme (inputDirectory, inputDirectory)