# !bin/bash/python

dirs = {
    'R': (0,1),
    'L': (0,-1),
    'U': (1,0),
    'D': (-1,0)
}

def solution():
    with open("inputs/day3.txt", "r") as f:
        seens = []
        for z in f:
            l = z.split(",") # gets a line and splits each instruction
            x = 0
            y = 0
            visited = {}
            step = 0
            for ins in l:
                direction, dist = ins[0], ins[1:]
                dist = int(dist)
                dy, dx = dirs[direction]
                for _ in range(dist):
                    step += 1
                    x += dx
                    y += dy
                    if (x,y) not in visited:
                        visited[(x,y)] = step
            seens.append(visited)
        intersects = set(seens[0].keys()).intersection(set(seens[1].keys()))
    return min(abs(x)+abs(y) for (x,y) in intersects) , min(seens[0][k] + seens[1][k] for k in intersects)

print(solution())