def solve(numbers):
    n = len(numbers)
    print 'n', n
    c = 0
    steps = 0
    while 0 <= c < n:
        steps += 1
        next_step = numbers[c]
        numbers[c] += 1 if numbers[c] < 3 else -1
        c += next_step

    return steps

with open('day5.txt', 'r') as f:
    numbers = map(int, map(lambda l: l[:-1], f.readlines()))
    res = solve(numbers)
    print res
