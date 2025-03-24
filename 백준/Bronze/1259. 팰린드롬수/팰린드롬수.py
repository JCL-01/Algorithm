import sys
i = 0
while True:
    N = sys.stdin.readline().rstrip()
    if N == '0':
        break
    if i != 0:
        sys.stdout.write('\n')
    ascending = ''
    for i in range(int(len(N) / 2) + 1):
        ascending += N[i]
    descending = ''
    for j in range(-1, -(int(len(N) / 2) + 1) -1, -1):
        descending += N[j]
    if ascending == descending:
        sys.stdout.write('yes')
    else:
        sys.stdout.write('no')
    i += 1