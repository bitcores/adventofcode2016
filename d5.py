import hashlib

#ki = 'abc'
ki = 'wtnhxymk'
pswd = ["X","X","X","X","X","X","X","X"]
c = 0
found = False

for p in range(0,8):
    while not found:
        m = hashlib.md5()
        m.update(ki.encode('utf-8'))
        m.update(str(c).encode('utf-8'))
        
        check = m.hexdigest()[:5]

        c = c + 1
        if check.count('0') == 5:
            if m.hexdigest()[5].isdigit():
                if int(m.hexdigest()[5]) < 8 and pswd[int(m.hexdigest()[5])] == "X":
                    pswd[int(m.hexdigest()[5])] = m.hexdigest()[6]
                    print(pswd)
                    #print(m.hexdigest())
                    #input()
                    break
        
print(pswd)
