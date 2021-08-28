import math

def decider(s, n, k):
    if k == 0:
        return 'YES'
    if n < 3:
        return 'NO'
    if k >= n/2:
        return 'NO'
    count = 0
    for x in range((math.floor(len(s)/2))):
        if s[x] == s[-x-1]:
            count = count + 1
        else:
            break
    if count >= k:
        return "YES"
    else:
        return "NO"

T = int(input()) 
for t in range(1, T + 1):
    line = input()
    nk = line.split(" ")
    s = input()
    result = decider(s, int(nk[0]), int(nk[1]))
    print(result)
