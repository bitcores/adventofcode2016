
#test input
#inp = "abcde"
#inp = "decab"
#parta input
#inp = "abcdefgh"
#inp = "gbhcefad"
#partb input
inp = "fbgdceah"
partb = True

funct = []
with open("input21.txt") as fp:
    for line in fp:
        line = line.strip()
        funct.append(line)

outp = inp

fl1 = 0
fl2 = len(funct)
fl3 = 1

if partb:
    fl1 = len(funct)-1
    fl2 = -1
    fl3 = -1

for f in range(fl1, fl2, fl3):
    pts = funct[f].split(" ")

    if pts[0] == "swap":
        if pts[1] == "position":
            x = int(pts[2])
            y = int(pts[5])
            sx = outp[x]
            sy = outp[y]

        if pts[1] == "letter":
            sx = pts[2]
            sy = pts[5]
            x = outp.find(sx)
            y = outp.find(sy)

        if x < y:
            outp = outp[:x] + sy + outp[x+1:y] + sx + outp[y+1:]
        else:
            outp = outp[:y] + sx + outp[y+1:x] + sy + outp[x+1:]

    if pts[0] == "rotate":
        if pts[1] == "based":
            x = outp.find(pts[6])
            r = x+1
            if x >= 4:
                r += 1
            if r > len(outp):
                r = r - len(outp)
            # couldnt be bothered working out an equation for this
            if partb:
                if x == 1:
                    r = 1
                if x == 2:
                    r = 6
                if x == 3:
                    r = 2
                if x == 4:
                    r = 7
                if x == 5:
                    r = 3
                if x == 6:
                    r = 0
                if x == 7:
                    r = 4
            # this could be trouble
            if not partb:
                r = r*-1
            outp = outp[r:] + outp[:r]
        else:
            x = int(pts[2])
            if x > len(outp):
                x = x - len(outp)
            if partb:
                x = x*-1
            if pts[1] == "left":
                outp = outp[x:] + outp[:x]
            if pts[1] == "right":
                outp = outp[-x:] + outp[:-x]

    if pts[0] == "reverse":
        x = int(pts[2])
        y = int(pts[4])
        ss = outp[x:y+1]
        ss = ss[::-1]
        outp = outp[:x] + ss + outp[y+1:]
    
    if pts[0] == "move":
        x = int(pts[2])
        y = int(pts[5])

        if partb:
            t = x
            x = y
            y = t
        
        ss = outp[x]
        if x < y:
            outp = outp[:x] + outp[x+1:y+1] + ss + outp[y+1:]
        else:
            outp = outp[:y] + ss + outp[y:x] + outp[x+1:]

    print(outp)