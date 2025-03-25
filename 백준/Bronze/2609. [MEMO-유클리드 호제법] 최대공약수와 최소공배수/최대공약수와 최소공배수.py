import sys
A, B = map(int, sys.stdin.readline().split())
A_div = set()
for num in range(1, A + 1):
    if A % num == 0:
        A_div.add(num)
B_div = set()
for num in range(1, B + 1):
    if B % num == 0:
        B_div.add(num)
GCD = max(A_div & B_div)
bigger_num = max(A, B)
tmp = bigger_num
while True:
    if tmp % A == 0 and tmp % B == 0:
        break
    tmp += bigger_num
LCM = tmp
sys.stdout.write(f'{GCD}\n{LCM}')