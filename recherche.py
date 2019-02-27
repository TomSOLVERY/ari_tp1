# 9 - recherche.py
# Recuperation et traitment des requetes en calculant la correspondace RSV par un cosinus

import json, curses
from math import log, sqrt
from nltk.stem.porter import *

jsonDir = "../json/"

def recherche (stdscr, indir, M):
    
    # chargement de l'index inverse
    iifh = open(indir+"indexInverse.json", "r")
    indInv = json.load(iifh)
    iifh.close()

    # chargement du vocabulaire
    vocabfh = open(indir+"vocabulaire.json", "r")
    vocab = json.load(vocabfh)
    vocabfh.close()

    # chargement de l'anti-dictionnaire
    cwfh = open("../common_words", "r")
    cw = cwfh.read().split("\n")
    cwfh.close()

    # chargement des normes des docs
    normefh = open(indir+"norm.json", "r")
    normeDocs = json.load(normefh)
    normefh.close()

    N = len(normeDocs) # Taille du corpus

    # Boucle principale
    curses.echo() # Afficher ce qui est tapee
    stdscr.scrollok(True) # rendre le fenetre glissable
    stdscr.addstr("Bonjour, Veuillez entrer une requete \n")
    while True:
        query = stdscr.getstr()
        if (query == ""):
            break
        qTreatment(stdscr, query, M, indInv, vocab, cw, normeDocs, N)
    curses.endwin()

def qTreatment (stdscr, query, M, indInv, vocab, cw, normeDocs, N):
    # Application de l'anti-dictionnaire et troncature
    stemmer = PorterStemmer() # creation d'un objet stemmer (troncature)
    words = query.split(" ")
    termQ = [] # liste resultat
    for i in words:
        # anti-dictionnaire
        if (not (i.lower() in cw)):
            term = stemmer.stem(i.lower()) # troncature
            # Ajout si le terme fait partie de notre vocabulaire
            if (term in vocab):
                termQ.append(term)

    dictQ = {}  # Dictionnaire de la requete (terme: idf)
    for t in termQ:
        # si le mot apparait plusieur fois dans la requete
        if t in dictQ:
            dictQ[t] += dictQ[t]
        # si premier occurrence du mot
        else:
            dictQ[t] = log(N/vocab[t])

    # Calcul de la norme
    normQ = 0   # Norme de la requete
    for t in dictQ:
        normQ += dictQ[t]*dictQ[t]
    normQ = sqrt(normQ)

    # ===== Produit scalaire =====
    # Dictionnaire resultat (idDoc: produit scalaire)
    res = {}
    for t in dictQ:
        # recuperation du dictionnaire de l'indexe inverse associe au terme t
        tii = indInv[t]
        # Produit scalaire non normalise
        for idDoc in tii:
            if idDoc in res:
                res[idDoc] += dictQ[t]*tii[idDoc]
            else:
                res[idDoc] = dictQ[t]*tii[idDoc]
    
    # Normalisation
    for idDoc in res:
        res[idDoc] /= normQ*normeDocs[idDoc]

    # Tri par valeurs decroissantes
    sres = sorted(res.items(), key=lambda kv:kv[1], reverse=True)

    # Affichage (min au cas ou il y a moins de resultats que M)
    for i in range(min(len(sres), M)):
        stdscr.addstr(sres[i][0] + "\n")


def mainf(stdscr):
    recherche(stdscr, jsonDir, 5)

curses.wrapper(mainf)