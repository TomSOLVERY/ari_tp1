# 9 - recherche.py
# Recuperation et traitment des requetes en calculant la correspondace RSV par un cosinus

import json, curses, string, subprocess
from math import log, sqrt
from nltk.stem.porter import *
from mercurial.templater import word

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

    curses.echo() # Afficher ce qui est tapee
    stdscr.scrollok(True) # rendre le fenetre glissable
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK) # texte en couleur cyan
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK) # texte en couleur verte
    stdscr.addstr("Bonjour, Veuillez entrer\n - Une requete pour faire un recherche ou\n - Un numero de document pour l'ouvrir\n")
    
    # Boucle principale
    while True:
        query = stdscr.getstr()
        if (query == ""):
            break
        try:
            if int(query) in range(N):
                stdscr.addstr("Ouverture du document " + query + "\n")
                # Si vous utilisez un Mac, remplacer "xdg-open" par "open"
                subprocess.call(["xdg-open", "../clean/CACM-" + query + ".flt"])
        except:
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
                
    if not termQ:
        stdscr.addstr("Votre requete n'as monte aucun resultat\n")
        return

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
        if normQ*normeDocs[idDoc] != 0:
            res[idDoc] /= normQ*normeDocs[idDoc]
        else:
            stdscr.addstr("Le mot cacm n'est pas pertinent \n")
            M = 0
            break

    # Tri par valeurs decroissantes
    sres = sorted(res.items(), key=lambda kv:kv[1], reverse=True)

    # Affichage (min au cas ou il y a moins de resultats que M)
    for i in range(min(len(sres), M)):
        # Du nom du document et sot idf
        stdscr.addstr(sres[i][0] + "\t" + str(sres[i][1]) + "\n", curses.A_BOLD)
        
        # Des quelques mots en debut du document
        docfh = open("../clean/CACM-"+sres[i][0]+".flt", "r")
        doc = docfh.read().split(" ")
        docfh.close()
        
        # En couleur different si mot dans la requete
        for j in range (min(len(doc), 15)):
            if doc[j] in words:
                stdscr.addstr(doc[j]+" ", curses.color_pair(2))
            else:
                stdscr.addstr(doc[j]+" ", curses.color_pair(1))
        
        stdscr.addstr("\n")

def mainf(stdscr):
    recherche(stdscr, jsonDir, 5)

curses.wrapper(mainf)