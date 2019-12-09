# day1, part 2 shown.
with open("inputs/day1.txt") as f:
    fi = 0
    for line in f:
        m = (int(int(line)/3)-2)
        fi += m
        x = m
        while x:
            x = (int(x/3)-2)
            if x < 0:
                x = 0
            else:
                fi += x
    print(str(fi))
