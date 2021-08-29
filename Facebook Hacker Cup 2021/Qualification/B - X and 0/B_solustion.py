def flip(grid):
    flipped_grid = []
    flipped_grid = list(map(list, zip(*grid)))
    return flipped_grid
def req(grid, flipped_grid, N):
    possibilities = []
    singles = []
    for x in grid:
        if 'O' in x:
            continue
        else:
            counter = x.count(".")
            if counter == 1:
                temp = []
                dot_index = x.index(".")
                grid_index = grid.index(x)
                temp.append(dot_index)
                temp.append(grid_index)
                singles.append(temp)
            possibilities.append(counter)
    
    for x in flipped_grid:
        if 'O' in x:
            continue
        else:
            counter = x.count(".")
            if (counter == 1):
                temp = []
                dot_index = x.index(".")
                grid_index = flipped_grid.index(x)
                temp.append(grid_index)
                temp.append(dot_index)
                if temp in singles:
                    continue
            possibilities.append(counter)
    
    if not possibilities:
        return "Impossible"
    else:
        r = []
        m = min(possibilities)
        r.append(m)
        times = possibilities.count(m)
        r.append(times)
        return r

with open('input.txt','r') as inf:
    T = int(inf.readline())
    for x in range(1,T+1):
        N = int(inf.readline())
        grid = []
        for a in range(N):
            line = inf.readline().strip()
            grid.append(line)
        flipped_grid = flip(grid)
        result = req(grid, flipped_grid, N)
        if type(result) == str:
            with open('output.txt', 'a') as outf:
                outf.write('Case #{}: {}\n'.format(x,result))
        else:
            with open('output.txt', 'a') as outf:
                outf.write('Case #{}: {} {}\n'.format(x,result[0],result[1]))