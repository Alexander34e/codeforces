t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    p = 0
    k = []
    for l in range(n):
        k.append(a[l])
    for h in range(101):
        tmp = 0
        for g in range(n):
            if k[g] == -1:
                a[g] = h
        for j in range(n-2):
            difference = max(a[j], a[j+1], a[j+2])-min(a[j], a[j+1], a[j+2])
            mex = 0
            for u in range(101):
                if u not in a[j:j+3]:
                    mex = u
                    break
            if mex == difference:
                tmp += 1
        if tmp == n-2:
            p = 1
            print("YES")
            break
    if p == 0:
        print("NO")
