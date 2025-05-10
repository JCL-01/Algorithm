import sys
H, I, A, R, C = map(int, sys.stdin.readline().split())
sys.stdout.write(f'{H * I - A * R * C}')