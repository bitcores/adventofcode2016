# part 1 is 272, part 2 is 35651584
disklen = 272
#disklen = 35651584
#inp = "10000"
inp = "10001110011110000"

def genSum(d):
    chksum = "" 
    for z in range(0, len(d), 2):
        # check z+1 makes sense
        if z < len(d)-1:
            pair = d[z:z+2]
            if pair[0] == pair[1]:
                chksum += "1"
            else:
                chksum += "0"
    if len(chksum) % 2 == 0:
        return(genSum(chksum))
    return(chksum)

def genData(a):
    b = a[len(a)::-1]
    nb = []
    for x in range(0, len(b)):
        if b[x] == "0":
            nb.append("1")
        else:
            nb.append("0")
    b = ""
    for y in nb:
        b += y
    c = a + "0" + b
    if len(c) < disklen:
        return(genData(c))
    return(c[:disklen])
    

data = genData(inp)
#print(data)
chksum = genSum(data)
print(chksum)


