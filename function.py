def func(s):
    buf = list(map(float, s.split()))
    n = int(buf[0])
    A = buf[1:n+1]
    B = buf[n+1]
    x = buf[n+2:n+n+2]
    y = buf[n+n+2:]
    sx = sum([x[i] * A[i] for i in range(n)])
    sy = sum([y[i] * A[i] for i in range(n)])
    dB = 0.0001
    if((sx <= B + dB and sx >= B - dB) and (sy <= B + dB and sy >= B - dB)):
        b = y
        a = [x[i] - b[i] for i in range(n)]

        res = ''
        for i in range(n):
            res += str(int(A[i])) + '*A' + str(i) + '+'
        res += ' = ' + str(int(B)) + ' ---> '
        for i in range (n):
            res += 'x' + str(i) + '=' + str(a[i]) + '*t+' + str(b[i]) + ' '
        return res
    return ''

with open('input.txt') as sr, open('output.txt', 'w') as sw:
    for line in sr:
        print('.', end='')
        sw.write(func(line.strip())+'\n')