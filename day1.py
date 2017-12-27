captcha = raw_input()

result = 0
n = len(captcha)

for i in xrange(len(captcha)):
    next_index = (i+1) % n
    if captcha[i] == captcha[next_index]:
        result += ord(captcha[i]) - ord('0')

print result
