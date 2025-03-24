import sys
i = 0
while True:
    N = sys.stdin.readline().rstrip()
    if N == '0':
        break
    ascending = ''
    for i in range(int(len(N) / 2) + 1):
        ascending += N[i]
    descending = ''
    for j in range(-1, -(int(len(N) / 2) + 1) -1, -1):
        descending += N[j]
    if ascending == descending:
        sys.stdout.write('yes\n')
    else:
        sys.stdout.write('no\n')