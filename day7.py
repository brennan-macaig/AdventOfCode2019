import intcode

def permutations(elements):
    if len(elements) <= 1:
        yield elements
    else:
        for perm in permutations(elements[1:]):
            for i in range(len(elements)):
                yield perm[:i] + elements[0:1] + perm[i:]

with open("inputs/day7.txt", "r") as f:
    for line in f:
        l = intcode.process(line)
        largest_output = 0
        max_phase = []
        perms = list(permutations([0,1,2,3,4]))
        for i in range(0, len(perms)):
            in1 = intcode.execute_ret_output(l, [0, perms[i][0]])
            in2 = intcode.execute_ret_output(l, [in1, perms[i][1]])
            in3 = intcode.execute_ret_output(l, [in2, perms[i][2]])
            in4 = intcode.execute_ret_output(l, [in3, perms[i][3]])
            in5 = intcode.execute_ret_output(l, [in4, perms[i][4]])
            if in5 > largest_output:
                max_phase = perms[i]
                largest_output = in5
        print("phase: " + str(max_phase) + " output: " + str(largest_output))
