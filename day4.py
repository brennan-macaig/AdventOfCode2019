with open("inputs/day4.txt", "r") as f:
    for line in f:
        l = line.split("-")
        lowlim = int(l[0])
        upplim = int(l[1])
        fin = []
        for check in range(lowlim, upplim):
            consec = []
            decrease = True
            check = str(check)
            for i in range(0,6):
                if i != 0:
                    # compute decrease
                    if check[i] < check[i-1]:
                        decrease = False
                if i != 5:
                    if check[i] == check[i+1]:
                        consec.append(1)
            if consec.__len__() >= 1:
                if decrease == True:
                    fin.append(check)
        print(fin.__len__())