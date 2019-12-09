"""
OPCODE SPEC:

MODE_OPCODE,OP1,OP2,TARG

MODE_OPCODE: starts with 3 digits, either 0 or 1, to specify modes
of commands. Then, the final two digits, are the opcode. Ex:
MMMOP, or 00102 would be evauluated as 0-0-1-MULT

OP1: First operand

OP2: Second operand

TARG: Store to this target

VALID COMMANDS:

1: add op1, op2, targ --> adds op1 and op2, stores in targ
2: mul op1, op2, targ --> multiplies op1 and op2, stores in targ
3: inp targ           --> input a single digit, store to targ
4: out targ           --> display single digit from targ.
5: jmp op1, targ      --> jump to instruction at targ if op1 != 0
6: jmp op1, targ      --> jump to instruction at targ if op1 == 0
7: les op1, op2, targ --> if op1 is less than op2, store 1 to targ. Else store 0
8: eql op1, op2, targ --> if op1 equals op2 store 1 to targ, else store 0

EXECUTE SPEC:

Execute takes in a processed list of opcode, and a list of valid inputs. It will
run the opcode, and using the list of inputs, provide any input to the function.
If it runs out of inputs, it will prompt the user.

RETURN VAL:
"""
def execute(intcode, args):
    i = 0
    in_num = 0
    for _ in range(0, intcode.__len__()):
        mode = str(intcode[i])
        leng = mode.__len__()
        pos = 0
        while leng < 5:
            # left-pad with 0's
            mode = "0" + mode
            leng = mode.__len__()
        p3m, p2m, p1m, op2, op1 = str(mode)
        p3m = int(p3m)
        p2m = int(p2m)
        p1m = int(p1m)
        
        opcode = int(op2 + op1)
        if opcode == 1:
            # add
            p1 = 0
            p2 = 0
            p3 = 0
            if p1m == 1:
                p1 = intcode[i+1]
            if p2m == 1:
                p2 = intcode[i+2]
            if p3m == 1:
                p3 = intcode[i+3]
            if p1m == 0:
                p1 = intcode[intcode[i+1]]
            if p2m == 0:
                p2 = intcode[intcode[i+2]]
            if p3m == 0:
                p3 = intcode[intcode[i+3]]
            opr = p1 + p2
            intcode[intcode[i+3]] = opr
            i = i+4
        elif opcode == 2:
            # mult
            p1 = 0
            p2 = 0
            p3 = 0
            if p1m == 1:
                # immediate mode
                p1 = intcode[i+1]
            if p2m == 1:
                p2 = intcode[i+2]
            if p3m == 1:
                p3 = intcode[i+3]
            if p3m == 0:
                p3 = intcode[intcode[i+3]]
            if p1m == 0:
                p1 = intcode[intcode[i+1]]
            if p2m == 0:
                p2 = intcode[intcode[i+2]]
            opr = p1 * p2
            intcode[intcode[i+3]] = opr
            i = i+4
        elif opcode == 3:
            # input
            p1 = 0
            p2 = 0
            text_in = ""
            if p1m == 1:
                p1 = intcode[i+1]
            if p1m == 0:
                p1 = intcode[intcode[i+1]]
            if args.__len__() > 0:
                if in_num <= args.__len__():
                    text_in = int(args[in_num])
                else:
                    text_in = int(input(">: "))
            else:
                text_in = int(input(">: "))
            intcode[intcode[i+1]] = text_in
            i = i + 2
        elif opcode == 4:
            # output
            p1 = 0
            p2 = 0
            if p1m == 1:
                p1 = intcode[i+1]
            if p1m == 0:
                p1 = intcode[intcode[i+1]]
            text_out = str(p1)
            print("sys.out: " + text_out + "\n")
            i = i + 2  
        elif opcode == 5:
            if p1m == 1:
                p1 = intcode[i+1]
            if p1m == 0:
                p1 = intcode[intcode[i+1]]
            if p1 != 0:
                if p2m == 1:
                    i = intcode[i+2]
                if p2m == 0:
                    i = intcode[intcode[i+2]]
            else:
                i = i + 3
        elif opcode == 6:
            if p1m == 1:
                p1 = intcode[i+1]
            if p1m == 0:
                p1 = intcode[intcode[i+1]]
            if p1 == 0:
                if p2m == 1:
                    i = intcode[i+2]
                if p2m == 0:
                    i = intcode[intcode[i+2]]
            else:
                i = i + 3
        elif opcode == 7:
            p1 = 0
            p2 = 0
            if p1m == 1:
                p1 = intcode[i+1]
            if p2m == 1:
                p2 = intcode[i+2]
            if p1m == 0:
                p1 = intcode[intcode[i+1]]
            if p2m == 0:
                p2 = intcode[intcode[i+2]]
            if p1 < p2:
                intcode[intcode[i+3]] = 1
            else:
                intcode[intcode[i+3]] = 0
            i = i + 4
        elif opcode == 8:
            p1 = 0
            p2 = 0
            if p1m == 1:
                p1 = intcode[i+1]
            if p2m == 1:
                p2 = intcode[i+2]
            if p1m == 0:
                p1 = intcode[intcode[i+1]]
            if p2m == 0:
                p2 = intcode[intcode[i+2]]
            if p1 == p2:
                intcode[intcode[i+3]] = 1
            else:
                intcode[intcode[i+3]] = 0
            i = i + 4
        elif opcode == 99:
            print("**sys halt**\n[diagnostics]")
            print("mem[0]: " + str(intcode[0]))
            return intcode
        else:
            print("**sys crash**")
            print("error reading intcode")
            print("[diagnostics]")
            print("opcode: " + str(opcode) + " @ mem index: " + str(i))
            return 0

def execute_ret_output(intcode, args):
    i = 0
    in_num = 0
    for _ in range(0, intcode.__len__()):
        mode = str(intcode[i])
        leng = mode.__len__()
        while leng < 5:
            # left-pad with 0's
            mode = "0" + mode
            leng = mode.__len__()
        p3m, p2m, p1m, op2, op1 = str(mode)
        p3m = int(p3m)
        p2m = int(p2m)
        p1m = int(p1m)
        
        opcode = int(op2 + op1)
        if opcode == 1:
            # add
            p1 = 0
            p2 = 0
            if p1m == 1:
                p1 = intcode[i+1]
            if p2m == 1:
                p2 = intcode[i+2]
            if p3m == 1:
                p3 = intcode[i+3]
            if p1m == 0:
                p1 = intcode[intcode[i+1]]
            if p2m == 0:
                p2 = intcode[intcode[i+2]]
            if p3m == 0:
                p3 = intcode[intcode[i+3]]
            opr = p1 + p2
            intcode[intcode[i+3]] = opr
            i = i+4
        elif opcode == 2:
            # mult
            p1 = 0
            p2 = 0
            if p1m == 1:
                # immediate mode
                p1 = intcode[i+1]
            if p2m == 1:
                p2 = intcode[i+2]
            if p3m == 1:
                p3 = intcode[i+3]
            if p3m == 0:
                p3 = intcode[intcode[i+3]]
            if p1m == 0:
                p1 = intcode[intcode[i+1]]
            if p2m == 0:
                p2 = intcode[intcode[i+2]]
            opr = p1 * p2
            intcode[intcode[i+3]] = opr
            i = i+4
        elif opcode == 3:
            # input
            p1 = 0
            p2 = 0
            text_in = ""
            if p1m == 1:
                p1 = intcode[i+1]
            if p1m == 0:
                p1 = intcode[intcode[i+1]]
            if args.__len__() > 0:
                if in_num <= args.__len__():
                    text_in = int(args[in_num])
                    in_num += 1
                else:
                    text_in = int(input(">: "))
            else:
                text_in = int(input(">: "))
            intcode[intcode[i+1]] = text_in
            i = i + 2
        elif opcode == 4:
            # output
            p1 = 0
            p2 = 0
            if p1m == 1:
                p1 = intcode[i+1]
            if p1m == 0:
                p1 = intcode[intcode[i+1]]
            return p1
        elif opcode == 5:
            if p1m == 1:
                p1 = intcode[i+1]
            if p1m == 0:
                p1 = intcode[intcode[i+1]]
            if p1 != 0:
                if p2m == 1:
                    i = intcode[i+2]
                if p2m == 0:
                    i = intcode[intcode[i+2]]
            else:
                i = i + 3
        elif opcode == 6:
            if p1m == 1:
                p1 = intcode[i+1]
            if p1m == 0:
                p1 = intcode[intcode[i+1]]
            if p1 == 0:
                if p2m == 1:
                    i = intcode[i+2]
                if p2m == 0:
                    i = intcode[intcode[i+2]]
            else:
                i = i + 3
        elif opcode == 7:
            p1 = 0
            p2 = 0
            if p1m == 1:
                p1 = intcode[i+1]
            if p2m == 1:
                p2 = intcode[i+2]
            if p1m == 0:
                p1 = intcode[intcode[i+1]]
            if p2m == 0:
                p2 = intcode[intcode[i+2]]
            if p1 < p2:
                intcode[intcode[i+3]] = 1
            else:
                intcode[intcode[i+3]] = 0
            i = i + 4
        elif opcode == 8:
            p1 = 0
            p2 = 0
            if p1m == 1:
                p1 = intcode[i+1]
            if p2m == 1:
                p2 = intcode[i+2]
            if p1m == 0:
                p1 = intcode[intcode[i+1]]
            if p2m == 0:
                p2 = intcode[intcode[i+2]]
            if p1 == p2:
                intcode[intcode[i+3]] = 1
            else:
                intcode[intcode[i+3]] = 0
            i = i + 4
        elif opcode == 99:
            print("**sys halt**\n[diagnostics]")
            print("mem[0]: " + str(intcode[0]))
            return intcode
        else:
            print("**sys crash**")
            print("error reading intcode")
            print("[diagnostics]")
            print("opcode: " + str(opcode) + " @ mem index: " + str(i))
            return 0


"""
Given a string to pre-process, this processes it and returns executable
intcode, for use in other functions.
"""
def process(intcode_string):
    y = map(int, intcode_string.split(","))
    return list(y)
