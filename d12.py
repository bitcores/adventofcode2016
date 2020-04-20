
reg = {'a':0,'b':0,'c':1,'d':0}
instru = []

with open("input12.txt") as fp:
    for line in fp:
        instru.append(line.strip())

ptr = 0

while ptr < len(instru):
    rd = instru[ptr]
    brk = rd.split(' ')

    if brk[0] == 'cpy':
        t = brk[1]
        if t.isdigit():
            t = int(t)
        else:
            t = reg[t]
        reg[brk[2]] = t
    
    if brk[0] == 'inc':
        reg[brk[1]] = reg[brk[1]] + 1

    if brk[0] == 'dec':
        reg[brk[1]] = reg[brk[1]] - 1
    
    if brk[0] == 'jnz':
        t = brk[1]
        if t.isdigit():
            t = int(t)
        else:
            t = reg[t]
        if t != 0:
            ptr = ptr + int(brk[2])
        else:
            ptr += 1
    else:
        ptr += 1

print(reg)
