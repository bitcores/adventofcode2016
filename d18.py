
#inp = '.^^.^.^^^^'
inp = '^.^^^..^^...^.^..^^^^^.....^...^^^..^^^^.^^.^^^^^^^^.^^.^^^^...^^...^^^^.^.^..^^..^..^.^^.^.^.......'

trows = 40
rows = []

row = []
row.append('.')
for x in inp:
    row.append(x)
row.append('.')
rows.append(row)

for y in range(0,trows-1):
    row = []
    row.append('.')
    for x in range(1,len(inp)+1):
        l = rows[y][x-1]
        r = rows[y][x+1]

        if l == r:
            row.append('.')
        else:
            row.append('^')
    row.append('.')
    rows.append(row)

safecnt = 0
for x in range(0,len(rows)):
    line = ""
    for p in range(1,len(rows[x])-1):
        line += rows[x][p]
        if rows[x][p] == '.':
            safecnt += 1
    #print(line)
print("Safe tiles ", safecnt)