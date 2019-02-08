import os
from math import log
inputDirectory = "../clean/"

def zipf(indir):
    vocab = {}
    m = 0
    for file in os.listdir(indir):
        fileHandler = open(indir+file, "r")
        #print ("processing file"+file)
        doc = fileHandler.read() 
        words = doc.split(" ")
        for i in words:
            m = m+1
            if i in vocab:
                vocab[i] = vocab[i] + 1
            else:
                vocab[i] = 1
    
    sorted_vocab = sorted(vocab.items(), key=lambda kv:kv[1], reverse=True)
    print("Les 10 mots les plus frequents:")
    print(sorted_vocab[0:9])
    print("\nLa taille du vocabulaire: %d \n" %(len(sorted_vocab)))
    lbda = m/log(len(sorted_vocab))
    print("Lambda = %d" %(lbda))

zipf(inputDirectory)