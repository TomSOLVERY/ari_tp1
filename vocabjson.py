# 5 - vocabjson.py
# Construction du vocabulaire associe a la collection .sttr en considerant tous les termes
# qui apparaissent au moins une fois. Le resultat est stocke dans un fichier “vocabulaire.json”
# format terme: document_frequency

import os
import json

inputDirectory = "../antiDict/"
outputDirectory = "../json/"

def vocabjson(indir, outdir):
    vj = {} # dictionnaire du vocabulaire.json

    for file in os.listdir(indir):
        vjfh = open(indir+file, "r") # vj fileHandler
        # Un set ne contient pas de duplicats. a voir comme list.uniq()
        words = set(vjfh.read().split(" "))
        vjfh.close()

        # words ne contient pas de duplicats. Chaque i dans word est unique au sein du document.
        # Donc la valeur vj[i] correspond bien au nombre du documents ou i apparait
        for i in words:
            if i in vj:
                vj[i] = vj[i] + 1
            else:
                vj[i] = 1    
    vj.pop("") # Supprimer le mot vide car aucun interet

    # Ecriture dans le fichier json
    f = open(outdir+"vocabulaire.json", "w+")
    json.dump(vj, f)
    f.close()

vocabjson(inputDirectory, outputDirectory)