def is_valid(passphrase):
    tokens = passphrase.split()
    return len(tokens) == len(set(tokens))

def solve(lines):
    result = 0
    for line in lines:
        if is_valid(line):
            result += 1
    return result

with open('day4.txt', 'r') as f:
    lines = map(lambda line: line[:-1], f.readlines())
    res = solve(lines)

    print res
