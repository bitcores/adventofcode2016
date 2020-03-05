import re

tsides = []
ptri = 0
pcnter = 0
with open("input3.txt") as fp:
    for line in fp:
        line = line.strip()
        tmp = re.findall(r'-?\d+', line)
        numbers = list(map(int, tmp))
        tsides.append(numbers)
        pcnter +=1
        if pcnter == 3:
            for x in range(0,3):   
                if tsides[0][x] + tsides[1][x] > tsides[2][x] and tsides[0][x] + tsides[2][x] > tsides[1][x] and tsides[1][x] + tsides[2][x] > tsides[0][x]:
                    ptri += 1
            tsides.clear()
            pcnter = 0
        

print(ptri)