# day2B
# split this into a different file because I have a
# hunch we'll use our intcode computer.
import intcode

with open("inputs/day2.txt") as f:
    targ = 19690720 # final number to reach
    for line in f:
        for noun in range(0,100):
            for verb in range(0,100):
                y = map(int, line.split(","))
                l = list(y)
                l[1] = noun
                l[2] = verb
                if intcode.execute(l) == targ:
                    print("noun: " + str(noun) + " verb: " + str(verb))
                    break
