import os
import json

inputDirectory = "../antiDict/"

def vocabjson(indir):
    vj = {}
    m = 0
    for file in os.listdir(indir):
        vjfh = open(indir+file, "r") 
        words = vjfh.read().split(" ")
        vjfh.close()
        for i in words:
            m = m+1
            if i in vj:
                vj[i] = vj[i] + 1
            else:
                vj[i] = 1
    
    f = open("../vocabulaire.json", "w+")
    json.dump(vj, f)
    f.close()

vocabjson(inputDirectory)