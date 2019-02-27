# 6 - vect.py
# construction de la representation vectorielle de tous les documents d'apres le modele vectoriel de Salton.
# Le type de representation choisi est une representation creuse (sparse) de chaque document d 
# avec un dictionnaire de couples (terme, tf.idf du terme dans d), ou idf_i = ln(N/df_i) 
# On ne se preoccupe pas encore de la normalisation.

import os
from math import log
import json

inputDirectory = "../antiDict/"
outputDirectory = "../json/"

def SaltonVect(indir, outdir):
    # un dictionnaire qui stocke l'ensemble de tous les vecteurs de documents
    # avec l'identifiant de document comme cle
    res = {}
    # chargement du corpus des documents
    docs = os.listdir(indir)
    N = len(docs)
    # chargement du vocabulaire
    vf = open(outdir+"vocabulaire.json", "r")
    vocab = json.load(vf)
    vf.close()
    # Pour tout fichier sttr
    for file in docs:
        # le vecteur du document courant
        dvect = {}
        # words contient les mots du fichier sttr
        fh = open(indir+file, "r")
        words = fh.read().split(" ")
        fh.close()
        words.remove("") # Supprimer le mot vide car aucun interet
        for i in words:
            # calcul du idf_i
            idf_i = log(N/vocab[i])
            # Si le mot a ete vu dans le doc, ajouter idf_i
            if i in dvect:
                dvect[i] = dvect[i] + idf_i
            # Si c'est la premiere occurrence du mot dans le doc, assigner idf_i
            else:
                dvect[i] = idf_i
        # ajout du vecteur du doc dans res avec l'identifiant de document comme cle
        res[int(file.strip("CACM-").strip(".sttr"))] = dvect
    # verification du resultat
    f = open(outdir+"vect.json", "w+")
    json.dump(res, f)
    f.close()

SaltonVect(inputDirectory, outputDirectory)