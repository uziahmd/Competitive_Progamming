import math
def countDistinct(arr, n):
    s = set()
    res = 0
    for i in range(n):
        if (arr[i] not in s):
            s.add(arr[i])
            res += 1
    return res 

def mex(A):
    m = max(A)
    if m < 0:
        return 0
    if len(A) == 1:
        return 1 if A[0] == 0 else 0
    cl = [0] *(m+1)
    for i in range(len(A)):
        if cl[A[i]] != 1:
            cl[A[i]] = 1
    for i in range(len(cl)):
        if cl[i] == 0:
            return i
    return i + 1

def calc(m, n, k):
    for x in range(k):
        a = max(m)
        b = mex(m)
        number = math.ceil((a+b)/2)
        m.append(number)
    result = countDistinct(m, len(m))
    return result

T = int(input()) 
for t in range(1, T + 1):
    line = input()
    nk = line.split(" ")
    nk = [int(i) for i in nk] 
    m = input().split(" ")
    m = [int(i) for i in m] 
    result = calc(m, nk[0], nk[1])
    print(result)