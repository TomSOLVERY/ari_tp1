inpfilename = "../cacm.all"
outpathname = "../split/"

def ExtractionDesFichiers(infile,outpath):
    fileHandler = open (infile, "r")
    debut = True
    while True:
        line = fileHandler.readline()
        if not line :
            break
        #print 'XXXXX',line[:-1]
        if line[0:2] == '.I':
            if not debut:
                f.close()
            debut = False
            a,b = line.split(" ")
            print ("processing file CACM-"+b[:-1])
            f = open(outpath+"CACM-"+b[:-1],"w+")
        if line[:-1] == '.T' or line[:-1] == '.A' or line[:-1] == '.W' or line[:-1] == '.B':
            out = True
            #print 'TOTO'
            while out:
                line = fileHandler.readline()
                #print line
                if not line :
                    break
                if line[:-1] == '.N' or line[:-1] == '.X' or line[:-1] == '.K' or line[:-1] == '.I':
                    out = False
                    #print 'OUT',line[:-1]
                    break
                elif line[:-1] != '.T' and line[:-1] != '.A' and line[:-1] != '.W' and line[:-1] != '.B':
                    f.write(line[:-1]+"\n")
    fileHandler.close()

ExtractionDesFichiers(inpfilename,outpathname)