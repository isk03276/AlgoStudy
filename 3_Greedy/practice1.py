import sys

N, M, K = list(map(int, sys.stdin.readline().split()))
input_list = list(map(int, sys.stdin.readline().split()))
assert len(input_list) == N

input_list.sort()
first_max_num = input_list[-1]
second_max_num = input_list[-2]

result = (M // (K+1))*(K*first_max_num + second_max_num)
result += (M % (K+1))*first_max_num

print(result)
