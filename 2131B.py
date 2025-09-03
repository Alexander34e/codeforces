t = int(input())
for i in range(t):
    n = int(input())
    p = [-1]*n
    for j in range(1, n, 2):
        if j+1 < n:
            p[j] = abs(p[j-1]+p[j+1])+1
        else:
            p[j] = abs(p[j-1])+1
    print(' '.join(list(map(str, p))))
    