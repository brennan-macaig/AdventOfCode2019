with open("inputs/day4.txt", "r") as f:
    for line in f:
        l = line.split("-")
        lowlim = int(l[0])
        upplim = int(l[1])
        fin = []
        
        for check in range(lowlim, upplim):
            decrease = True
            check = str(check)
            row = {
                "1": 0,
                "2": 0,
                "3": 0,
                "4": 0,
                "5": 0,
                "6": 0,
                "7": 0,
                "8": 0,
                "9": 0,
                "0": 0
            }
            
            for i in range(0,6):
                if i != 0:
                    if check[i] < check[i-1]:
                        decrease = False
                if i != 5:
                    if check[i] == check[i+1]:
                        if row[check[i]] == 1 or row[check[i]] == 99:
                            row[(check[i])] = 99
                        else:
                            row[check[i]] = 1

            if not 1 in row.values():
                if decrease == True:
                    fin.append(check)
        print(fin)
        print(fin.__len__())