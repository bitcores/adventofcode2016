from math import floor

def isInt(s):
    if s[0] in ('-', '+'):
        return s[1:].isdigit()
    return s.isdigit()

reg = {'a':0,'b':0,'c':0,'d':0}
instru = []
clkval = 0
lclock = None
lccnt = 0

with open("input25.txt") as fp:
    for line in fp:
        line = line.strip()
        brk = line.split(' ')
        instru.append(brk)

while True:
    # lets set the register and ptr states on start for protection
    ptr = 0
    reg['a'] = clkval
    reg['b'] = 0
    reg['c'] = 0
    reg['d'] = 0

    while ptr < len(instru):
        rd = instru[ptr]
        #print(rd)
        #print(reg)
        #print(instru)
        #input()
        if rd[0] == 'cpy':
            t = rd[1]
            r = rd[2]

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
            # multiplication
            if rd1[0] == 'dec' and rd2[0] == 'jnz' and rd2[2] == '-2' and rd3[0] == 'dec' and rd4[0] == 'jnz' and rd4[2] == '-5':
                reg[rd[1]] = reg[rd[1]] + (reg[rd1[1]] * reg[rd3[1]])
                reg[rd1[1]] = 0
                reg[rd3[1]] = 0
                ptr += 5
                continue
            if rd[1] in reg:
                reg[rd[1]] = reg[rd[1]] + 1

        if rd[0] == 'dec':
            rd1 = instru[ptr+1]
            rd2 = instru[ptr+2]
            rd3 = instru[ptr+3]
            rd4 = instru[ptr+4]
            # division
            if rd1[0] == 'dec' and rd2[0] == 'jnz' and rd2[2] == '-4' and rd3[0] == 'inc' and rd4[0] == 'jnz' and rd4[2] == '-7':
                reg[rd3[1]] = reg[rd3[1]] + floor(reg[rd[1]] / reg[rd1[1]])                
				# if the register rd[1] (d) divides evenly by rd1[1] (c)
                # there is no remainder, the value of register rd1[1] (c) is 2, else 1
                if reg[rd[1]] % reg[rd1[1]] == 0:
                    reg[rd1[1]] = 2
                else:
                    reg[rd1[1]] = 1
                reg[rd[1]] = 0
                ptr += 5
                continue
            if rd[1] in reg:
                reg[rd[1]] = reg[rd[1]] - 1
        
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
                continue
        
        if rd[0] == 'out':
            t = rd[1]
            if isInt(t):
                t = int(t)
            else:
                t = reg[t]

            if t == lclock:
                lclock = None
                lccnt = 0
                break
            else:
                lclock = t
                lccnt +=1
                # testing for infinite 0,1 pattern (set any large number)
                if lccnt > 500:
                    print("Clock input val: ", clkval)
                    input()
        
        ptr += 1
    
    clkval += 1

