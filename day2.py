result = 0
with open('day2.txt') as f:
    lines = f.readlines()

    for line in lines:
        tokens = map(int, str(line[:-1]).split('\t'))
        result += max(tokens) - min(tokens)

print result
