def get_max_index(arr):
    mval = -100
    res = -1
    for i, num in enumerate(arr):
        if num > mval:
            res = i
            mval = num

    return res

def redistribute(numbers, ind):
    n = len(numbers)
    dval = numbers[ind]
    numbers[ind] = 0
    min_val = dval // n
    plus_one_count = dval - min_val*n

    current = (ind+1) % n
    for i in xrange(n):
        if i < plus_one_count:
            numbers[current] += min_val + 1
        else:
            numbers[current] += min_val

        current = (current + 1) % n

    return numbers

def hash(numbers):
    return '-'.join(map(str, numbers))

def solve(numbers):
    seen = set()
    seen.add(hash(numbers))

    count = 0
    while True:
        max_ind = get_max_index(numbers)
        numbers = redistribute(numbers, max_ind)
        h = hash(numbers)
        count += 1
        if h in seen:
            break
        seen.add(h)

    return count

with open('day6.txt', 'r') as f:
    numbers = map(int, f.readlines()[0][:-1].split())
    res = solve(numbers)
    print res
