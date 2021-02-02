import sys

N = list(map(int, sys.stdin.readline().split()))
command_list = list(sys.stdin.readline().split())

current_position = [1, 1]

for command in command_list:
    if command == 'U':
        if current_position[0] == 1:
            continue
        else:
            current_position[0] -= 1
    elif command == 'D':
        if current_position[0] == N:
            continue
        else:
            current_position[0] += 1
    elif command == 'R':
        if current_position[1] == N:
            continue
        else:
            current_position[1] += 1
    elif command == 'L':
        if current_position[1] == 1:
            continue
        else:
            current_position[1] -= 1
print(current_position)




