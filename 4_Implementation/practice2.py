import sys

"""
4 4
1 1 0
1 1 1 1
1 0 0 1
1 1 0 1
1 1 1 1
"""

N, M = list(map(int, sys.stdin.readline().split()))
A, B, d = list(map(int, sys.stdin.readline().split()))

map_data = []


for _ in range(N):
    map_data.append(list(map(int, sys.stdin.readline().split())))

orientation_ops = [(0,-1), (1,0), (0,1), (-1,0)] # 북, 동, 남, 서

move_count = 1
rotation_count = 0
visited = [(A,B)]

while True:
    if rotation_count > 3:
        back_x = A + orientation_ops[abs(d + 2) % 4][0]
        back_y = B + orientation_ops[abs(d + 2) % 4][1]
        if back_x < 0 or back_x > M or back_y < 0 or back_y > N or (back_x,back_y) in visited or map_data[back_y][back_x] == 1:
            break
        else:
            A = back_x
            B = back_y
            move_count += 1
            rotation_count = 0
            visited.append((A,B))
    else:
        west_x = A + orientation_ops[abs(d + 3) % 4][0]
        west_y = B + orientation_ops[abs(d + 3) % 4][1]
        if west_x < 0 or west_x > M or west_y < 0 or west_y > N or (west_x, west_y) in visited or map_data[west_y][west_x] == 1:
            rotation_count += 1
        else:
            A = west_x
            B = west_y
            move_count += 1
            rotation_count = 0
            visited.append((A,B))
        d = abs(d + 3) % 4
print(move_count)
