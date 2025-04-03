import sys
n, m = map(int, sys.stdin.readline().split())
sys.stdout.write('{}\n{}'.format(n//m, n%m))