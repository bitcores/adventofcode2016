import re
from copy import deepcopy

charcnt = 0

def countsub(sstr, m):
    global charcnt

    while len(sstr) > 0:
        mul = deepcopy(m)
        rere = re.search(r"\((\w+)\)", sstr)
        if rere != None:
            girk = rere.group(1)
            npos = sstr.find(girk, 0)
            seqrep = girk.split("x")
            seq = int(seqrep[0])
            rep = int(seqrep[1])
            comp = len(girk)+2
            txtseq = sstr[npos+comp-1:npos+comp-1+seq]
            sstr = sstr[:npos-1] + sstr[npos+comp-1+seq:]
            mul.append(rep)
            rstr = countsub(txtseq, deepcopy(mul))
            #print("2", rstr)
            if len(rstr) > 0:
                #print(mul)
                rstrl = len(rstr)
                for x in mul:
                    rstrl = rstrl * x
                charcnt += rstrl     
        else:
            return sstr
        
    return ""

with open("input9.txt") as fp:
    for line in fp:
        line = line.strip()
        inp = line

        subbs = re.findall(r"\((\w+)\)", line)
        subig = []
        pos = 0
        for bs in subbs:        
            if bs in subig:
                subig.pop(0)
                continue

            npos = line.find(bs, pos)  
            seqrep = bs.split("x")
            seq = int(seqrep[0])
            rep = int(seqrep[1])
            comp = len(bs)+2
            txtseq = line[npos+comp-1:npos+comp-1+seq]
            subig = re.findall(r"\((\w+)\)", txtseq)
            ls = line[:npos-1]
            app = ""
            for x in range(0, rep):
                app += txtseq            
            #print(subig)
            #input()
            ls += app
            np = len(ls)-1
            #print(np)
            ls += line[npos+comp-1+seq:]
            pos = np
            line = ls
    
        #print(line)
        print(len(line))

        pos = 0             
        while len(inp) > 0:
            multilist = []
            rere = re.search(r"\((\w+)\)", inp)
            if rere != None:
                girk = rere.group(1)
                npos = inp.find(girk, 0)
                seqrep = girk.split("x")
                seq = int(seqrep[0])
                rep = int(seqrep[1])
                comp = len(girk)+2
                txtseq = inp[npos+comp-1:npos+comp-1+seq]
                #print(txtseq)
                inp = inp[:npos-1] + inp[npos+comp-1+seq:]
                multilist.append(rep)
                rstr = countsub(txtseq, deepcopy(multilist))
                if len(rstr) > 0:
                    rstrl = len(rstr) * rep
                    charcnt += rstrl
            else:
                charcnt += len(inp)
                break
        print(charcnt)
        