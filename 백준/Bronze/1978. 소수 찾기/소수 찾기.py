import sys
import math
_ = sys.stdin.readline()
num_list = list(map(int, sys.stdin.readline().split()))
decimal_num = 0
is_decimal = True
for i in num_list:
    if i == 1:
        continue
    if i == 2 or i == 3:
        decimal_num += 1
        continue
    for j in range(2, int(math.sqrt(i)) + 1):
        if i % j == 0:
            is_decimal = False
            break
    if is_decimal == True:
        decimal_num += 1
    is_decimal = True
    
sys.stdout.write(str(decimal_num))