import sys
sys.stdin.readline()
decimal_list = list(range(2, 1001))
decimal_num = 0
for i in range(2, 1001):
    for j in range(i+1, 1001):
        if j in decimal_list:
            if j % i == 0:
                decimal_list.remove(j)
for num in map(int, sys.stdin.readline().split()):
    if num in decimal_list:
        decimal_num += 1
sys.stdout.write(str(decimal_num))