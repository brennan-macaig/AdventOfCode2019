with open("inputs/day6.txt", "r") as f:
    final = 0
    orbs = {}
    for line in f:
        l = line.split(")")
        if l[0] in orbs:
            # this means the planet is already there.
            orbs[l[0]].append(l[1].rstrip())
        else:
            orbs.update({l[0]:[l[1].rstrip()]})
    for key, value in orbs.items():
        final += value.__len__()
    final += orbs.__len__()
    print(str(final))
