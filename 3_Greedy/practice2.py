import sys

N, M = list(map(int, sys.stdin.readline().split()))

max_num = 0
for i in range(N):
    temp = min(list(map(int, sys.stdin.readline().split())))
    if max_num < temp:
        max_num = temp

print(max_num)

