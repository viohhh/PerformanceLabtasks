import sys
n = int(sys.argv[1])
m = int(sys.argv[2])
k = m
ans = 1
while k != 1:
    ans = ans * 10 + k
    for i in range(m - 1):
        k = k + 1
        if k == n + 1:
            k = 1
print(ans)
