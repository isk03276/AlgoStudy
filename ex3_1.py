import sys

inputs = list(map(int, sys.stdin.readline().split()))

COINS = [500, 100, 50, 10]

for input_num in inputs:
    count = 0
    balance = input_num
    for coin in COINS:
        count += balance // coin
        balance = balance % coin
    print(count)




