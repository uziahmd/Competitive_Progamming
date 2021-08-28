import numpy as np
def rotate(list_1,n):  
    list_1 = (list_1[-n:] + list_1[:-n])  
    return list_1
def compute_trace(matrix):
    trace = 0
    for i in range(len(matrix)):
        trace += matrix[i][i]

    return trace

def solve(N, K):
    row = [i for i in range(1, N+1)]  
    matrix = []
    matrix.append(row)
    j=1
    while j< N:
       row = rotate(row,1)
       j+=1
       matrix.append(row)

    j = 1
    while j < N:
        trace = compute_trace(matrix)
        if trace == K:
           break
        else:
           matrix = rotate(matrix,1)
           j += 1
    if j < N:
       return ("POSSIBLE", matrix)
    else:
        np.flip(matrix)
        j = 1
        while j < N:

           trace = compute_trace(matrix)
           if trace == K:
              break
           else:
              matrix = rotate(matrix,1)
              j += 1
        if j < N:
           return ["POSSIBLE", matrix]
        else:
           return ["IMPOSSIBLE", ""]

T = int(input())
for i in range(T):
    N, K = [int(s) for s in input().split()]
    ans = solve(N, K)
    print("Case #{}: {}".format(str(i+1), ans[0]))
    if ans[0] == "POSSIBLE":
        for j in range(len(ans[1])):
            print(' '.join(str(n) for n in ans[1][j]))