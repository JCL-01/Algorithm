import sys
from math import factorial

N, K = map(int, sys.stdin.readline().split())
sys.stdout.write(str(int(factorial(N) / (factorial(N - K) * factorial(K)))))