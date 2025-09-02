t = int(input())
for i in range(t):
    n, c = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    count = 0
    j = n-1
    while j > -1:
        tmp = 0
        for h in range(len(a)):
            if abs(a[tmp]-c) > abs(a[h]-c) and a[h] <= c:
                tmp = h
        if a[tmp] > c:
            count += 1
        a.pop(tmp)
        for u in range(len(a)):
            a[u] *= 2
        j -= 1
    print(count)