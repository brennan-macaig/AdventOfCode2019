# intcode.py
# An extensible intcode computer.

"""
Executes an intcode sequence, given that the sequence is provided
as a preprocessed list of integers.
"""
def execute(intcode):
    i = 0
    for x in range(0,200):
            if intcode[i] == 1:
                # add
                opr = intcode[intcode[i+1]] + intcode[intcode[i+2]]
                intcode[intcode[i+3]] = opr
                i = i+4
            elif intcode[i] == 2:
                # mult
                opr = intcode[intcode[i+1]] * intcode[intcode[i+2]]
                intcode[intcode[i+3]] = opr
                i = i+4
            elif intcode[i] == 99:
                return intcode[0]
            else:
                return 0

"""
Given a string to pre-process, this processes it and returns executable
intcode, for use in other functions.
"""
def process(intcode_string):
    y = map(int, intcode_string.split(","))
    return list(y)