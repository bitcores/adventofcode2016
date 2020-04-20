
lightgrid = {}

def setlights(s, e, m):
    for y in range(int(s[1]), int(e[1])):
        if not y in lightgrid:
            lightgrid[y] = {}
        for x in range(int(s[0]), int(e[0])):
            if m == 1:
                lightgrid[y][x] = "#"
            elif m == 0:
                lightgrid[y][x] = "."

# x,y         
# 50,6
setlights([0,0], [50,6], 0)

with open("input8.txt") as fp:
    for line in fp:
        line = line.strip()
        sec = line.split(" ")
        if sec[0] == "rect":
            recxy = sec[1].split("x")
            setlights([0,0], [int(recxy[0]),int(recxy[1])], 1)
        if sec[0] == "rotate":
            crpos = sec[2].split("=")
            #crpos[1] = col/row
            #sec[4] = val
            cr = int(crpos[1])
            val = int(sec[4])
            buildline = ""
            if sec[1] == "row":
                for x in range(len(lightgrid[cr])):
                    buildline += lightgrid[cr][x]
                #line built ready for rotation
                for r in range(0,val):
                    buildline = buildline[-1:]+buildline[:-1]

                for x in range(len(lightgrid[cr])):
                    lightgrid[cr][x] = buildline[x]

            elif sec[1] == "column":
                for y in range(len(lightgrid)):
                    buildline += lightgrid[y][cr]
                #line built ready for rotation
                for r in range(0,val):
                    buildline = buildline[-1:]+buildline[:-1]
                
                for y in range(len(lightgrid)):
                    lightgrid[y][cr] = buildline[y]

oncount = 0
for y in range(len(lightgrid)):
    lineout = ""
    for x in range(0,len(lightgrid[y])):
        lineout += lightgrid[y][x]
    oncount += lineout.count("#")
    print(lineout)
print(oncount)