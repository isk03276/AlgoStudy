import sys

N, K = list(map(int, sys.stdin.readline().split()))

count = 0

"""
내가 생각한 방법
while True:
    if N % K == 0:
        N //= K
    else:
        N -= 1
    count += 1

    if N == 1:
        break
"""

"""
개선 방법
"""
while True:
    if N % K == 0:
        N //= K
        count += 1
    else: # 25 3
        target = (N // K) * K # 24
        count += (N-target) #
        N = target
    if N == 1:
        break
    elif N == 0:
        count -= 1
        break

print(count)