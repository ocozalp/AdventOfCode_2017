def solve(lines):
    incoming = dict()
    for line in lines:
        incoming[line[0]] = 0

    for line in lines:
        if len(line) > 2:
            for child in line[3:]:
                c = child
                if c[-1] == ',':
                    c = c[:-1]

                incoming[c] += 1

    for k in incoming:
        if incoming[k] == 0:
            return k

with open('day7.txt', 'r') as f:
    lines = map(lambda s: s.split(), map(lambda l: l[:-1], f.readlines()))
    res = solve(lines)
    print res
