import os
from nltk.tokenize import RegexpTokenizer
inputDirectory = "../split/"
outputDirectory = "../clean/"


def Numberless(indir, outdir):
    for file in os.listdir(indir):
        fileHandler = open(indir+file, "r")
        tokenizer = RegexpTokenizer('[A-Za-z]\w{0,}')
        print ("processing file"+file)
        f = open(outdir+file+".flt", "w+")
        while True:
            line = fileHandler.readline()
            if not line:
                break
            words = tokenizer.tokenize(line)
            for i in words :
                f.write(i.lower()+" ")
            #f.write("\n")
        f.close()
        fileHandler.close()

Numberless(inputDirectory,outputDirectory)
