# 3

import matplotlib.pyplot as plt
import os
from math import log
inputDirectory = "../clean/"

def zipf(indir):
    vocab = {} # dictionnaire terme: term frequency
    m = 0 # m le nombre total de mots

    for file in os.listdir(indir):
        fileHandler = open(indir+file, "r")
        doc = fileHandler.read() 
        words = doc.split(" ")
        # calcul de la fréquence d'apparition de tous les termes de la collection
        for i in words:
            m = m+1
            if i in vocab:
                vocab[i] = vocab[i] + 1
            else:
                vocab[i] = 1
    
    # tri du vocab par le tf decroissant
    sorted_vocab = sorted(vocab.items(), key=lambda kv:kv[1], reverse=True)

    # Convertir vocab en liste / tableau pour affichage (on garde que le tf)
    svtab = []
    for i in range(len(sorted_vocab)):
        svtab.append(sorted_vocab[i][1])

    # Affichage de quelques informations
    print("Les 10 mots les plus frequents:")
    print(sorted_vocab[0:9])
    print("\nLa taille du vocabulaire: %d \n" %(len(sorted_vocab)))
    lbda = m/log(len(sorted_vocab))
    print("Lambda = %d" %(lbda))

    # Affichage de courbes
    plt.title("Nombre d'occurrence total en fonction du rang")
    plt.ylabel("Nombre d'occurrence")
    plt.xlabel("Rang")
    plt.plot(svtab)
    plt.show()

    plt.title("Courbe de Zipf")
    plt.ylabel("Nombre d'occurences")
    plt.xlabel("Rang")
    tab2 = []
    for ind in range(len(svtab)):
        tab2.append(lbda/(ind+1))
    plt.plot(tab2)
    plt.show()

zipf(inputDirectory)


