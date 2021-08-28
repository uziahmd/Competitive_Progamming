
def time(X,Y,M):
    if (X+Y == 0):
        return 0
    for a in range(len(M)):
        if M[0]==N:
            Y=Y+1
        elif M[0]==S:
            Y=Y-1
        elif M[0]==E:
            X=X+1
        elif M[0]==W:
            X=X-1
        if (X+Y <=a+1):
            return a+1
    return 'IMPOSSIBLE'

T = int(input())
for t in range(1, T+1):
    X, Y, M = [s for s in input().split(" ")]
    X = int(X)
    Y = int(Y)
    result = time(X, Y, M)
    print("Case #{}: {}".format(t, result)