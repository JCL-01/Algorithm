import sys
N = int(sys.stdin.readline())
for i in range(max(1, N - 54), N + 1):
    if i == N:
        sys.stdout.write('0')
        break
    digit_sum = 0
    for digit in map(int, str(i)):
        digit_sum += digit
    if i + digit_sum == N:
        sys.stdout.write(str(i))
        break