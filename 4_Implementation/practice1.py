import sys

data = sys.stdin.readline().split()[0]

x = ord(data[0])
y = int(data[1])

ascii_a = ord('a')
ascii_z = ord('c')

operators = ((2,1), (2,-1), (-2,1,), (-2,-1), (1,2),(1,-2), (-1,2), (-1,-2))

count = 0

for op in operators:
    temp_x = x + op[0]
    temp_y = y + op[1]

    if temp_x < ascii_a or temp_x > ascii_z or temp_y < 1 or temp_y >8:
        continue
    else:
        count += 1

print(count)


