with open("inputs/day2.txt", "r") as f:
    for line in f:
        y = map(int, line.split(","))
        l = list(y)
        i = 0
        for x in range(0,200):
            if l[i] == 1:
                # add
                opr = l[l[i+1]] + l[l[i+2]]
                l[l[i+3]] = opr
                i = i+4
            if l[i] == 2:
                # mult
                opr = l[l[i+1]] * l[l[i+2]]
                l[l[i+3]] = opr
                i = i+4
            if l[i] == 99:
                print("arr: " + str(l))
                print("ans: " + str(l[0]))
                break
