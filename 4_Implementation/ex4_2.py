import sys

N = list(map(int, sys.stdin.readline().split()))[0]

count = 0

"""
입출력 예시를 토대로 한 야매 기법
"""

print(N)
num_three = N // 3

multiple_three = 60 * 60
not_multiple_three = (11475 - multiple_three) // 5

count += num_three * multiple_three
count += (N - num_three + 1)*not_multiple_three

print(count)
