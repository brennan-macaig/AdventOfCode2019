import intcode

with open("inputs/day5.txt", "r") as f:
    for line in f:
        l = intcode.process(line)
        print(intcode.execute(l))