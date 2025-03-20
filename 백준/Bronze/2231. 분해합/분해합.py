import sys
N = int(sys.stdin.readline())
constructor_list = []
for i in range(1, N):
    digit_num = 1
    tmp = i
    while True:
        if tmp / 10 >= 1:
            tmp /= 10
            digit_num += 1
            continue
        break
    digit_sum = 0
    tmp = i
    for _ in range(digit_num):
        digit_sum += tmp % 10
        tmp //= 10
    if i + digit_sum == N:
        constructor_list.append(i)
constructor_list.sort()
if constructor_list == []:
    sys.stdout.write('0')
else:
    sys.stdout.write(str(constructor_list[0]))