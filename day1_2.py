captcha = raw_input()

result = 0
n = len(captcha)
j = n // 2
for i in xrange(len(captcha)):
    next_index = (i+j) % n
    if captcha[i] == captcha[next_index]:
        result += ord(captcha[i]) - ord('0')

print result
