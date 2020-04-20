def isInt(s):
    if s[0] in ('-', '+'):
        return s[1:].isdigit()
    return s.isdigit()

reg = {'a':7,'b':0,'c':0,'d':0}
instru = []

with open("input23.txt") as fp:
    for line in fp:
        line = line.strip()
        brk = line.split(' ')
        instru.append(brk)

ptr = 0

while ptr < len(instru):
    rd = instru[ptr]
    #print(rd)
    #print(reg)
    #print(instru)
    #input()
    if rd[0] == 'cpy':
        t = rd[1]
        r = rd[2]
        if not isInt(t) and not isInt(r):
            rd1 = instru[ptr+1]
            rd2 = instru[ptr+2]
            rd3 = instru[ptr+3]

            if rd1[0] == 'dec' and rd2[0] == 'inc' and rd3[0] == 'jnz' and rd3[2] == '-2':
                reg[rd[1]] = reg[rd[1]] * 2
                reg[rd[2]] = 0
                ptr += 4
                continue
 
        if isInt(t) and isInt(r):
            ptr += 1
            continue
        if isInt(t):
            t = int(t)
        else:
            t = reg[t]
        reg[rd[2]] = t
    
    if rd[0] == 'inc':
        rd1 = instru[ptr+1]
        rd2 = instru[ptr+2]
        rd3 = instru[ptr+3]
        rd4 = instru[ptr+4]
        if rd1[0] == 'dec' and rd2[0] == 'jnz' and rd2[2] == '-2' and rd3[0] == 'dec' and rd4[0] == 'jnz' and rd4[2] == '-5':
            reg[rd[1]] = reg[rd[1]] + (reg[rd1[1]] * reg[rd3[1]])
            reg[rd1[1]] = 0
            reg[rd3[1]] = 0
            ptr += 5
            continue
        if rd[1] in reg:
            reg[rd[1]] = reg[rd[1]] + 1

    if rd[0] == 'dec':
        if rd[1] in reg:
            reg[rd[1]] = reg[rd[1]] - 1

    if rd[0] == 'tgl':
        oset = ptr+reg[rd[1]]
        if oset > len(instru)-1:
            ptr += 1
            continue

        gt = instru[oset]
        if len(gt) == 2: 
            if gt[0] == 'inc':
                instru[oset][0] = 'dec'
            else:
                instru[oset][0] = 'inc'
        if len(gt) == 3:
            if gt[0] == 'jnz':
                instru[oset][0] = 'cpy'
            else:
                instru[oset][0] = 'jnz'
        ptr += 1
        continue
    
    if rd[0] == 'jnz':
        t = rd[1]
        if isInt(t):
            t = int(t)
        else:
            t = reg[t]
        r = rd[2]
        if isInt(r):
            r = int(r)
        else:
            r = reg[r]
        if t != 0:
            ptr = ptr + r
        else:
            ptr += 1
    else:
        ptr += 1

print(reg)
