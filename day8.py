def eval_condition(registers, r, op, arg):
    if r in registers:
        v = registers[r]
    else:
        v = 0

    if op == '==':
        return arg == v

    if op == '!=':
        return arg != v

    if op == '>':
        return v > arg

    if op == '>=':
        return v >= arg

    if op == '<':
        return v < arg

    if op == '<=':
        return v <= arg

    raise Exception('Unexpected')

def evaluate(registers, r1, op1, arg1, r2, op2, arg2):
    if not eval_condition(registers, r2, op2, arg2):
        return

    if r1 in registers:
        v = registers[r1]
    else:
        v = 0

    if op1 == 'inc':
        v += arg1
    elif op1 == 'dec':
        v -= arg1
    else:
        raise Exception('Unexpected operator')

    registers[r1] = v


def solve(lines):
    registers = dict()
    for l in lines:
        evaluate(registers, l[0], l[1], int(l[2]), l[4], l[5], int(l[6]))


    mval = -10000000000000000
    res = -1
    for k in registers:
        if registers[k] > mval:
            mval = registers[k]
            res = k

    return mval

with open('day8.txt', 'r') as f:
    lines = map(lambda l: l[:-1].split(), f.readlines())
    res = solve(lines)
    print res
