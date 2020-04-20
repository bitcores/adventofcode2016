
def increPos():
    for x in discpos:
        discpos[x] = discpos[x]+1
        if discpos[x] == discposno[x]:
            discpos[x] = 0

def chpos(x):
    p = discpos[x]+x
    return(p % discposno[x])

discposno = {1: 13, 2: 17, 3: 19, 4: 7, 5: 5, 6: 3, 7: 11}
discpos = {1: 10, 2: 15, 3: 17, 4: 1, 5: 0, 6: 1, 7: 0}
time = 0

while True:
    r = 0
    for z in discpos:
        if chpos(z) == 0:
            r += 1
    if r == len(discpos):
        print(time)
        break
    increPos()
    time += 1