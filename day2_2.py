import itertools 

result = 0

with open('day2.txt') as f:
    lines = f.readlines()

    for line in lines:
        tokens = map(int, str(line[:-1]).split('\t'))

        for num1, num2 in itertools.combinations(tokens, 2):
            max_val = max(num1, num2)
            min_val = num1 + num2 - max_val
            if max_val % min_val == 0:
                result += max_val / min_val


print result
