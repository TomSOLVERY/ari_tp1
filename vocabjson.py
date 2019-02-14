import os
import json

inputDirectory = "../antiDict/"

def vocabjson(indir):
    vj = {}
    for file in os.listdir(indir):
        vjfh = open(indir+file, "r") 
        # Un set ne contient pas de duplicats. a voir comme list.uniq()
        words = set(vjfh.read().split(" "))
        vjfh.close()
        for i in words:
            if i in vj:
                vj[i] = vj[i] + 1
            else:
                vj[i] = 1
    vj.pop("")
    f = open("../vocabulaire.json", "w+")
    json.dump(vj, f)
    f.close()

vocabjson(inputDirectory)