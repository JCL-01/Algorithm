import sys
*num_pair, _ = sys.stdin.readlines()
for i in range(len(num_pair)):
    n, m = map(int, num_pair[i].split())
    sys.stdout.write('Yes\n') if n > m else sys.stdout.write('No\n')