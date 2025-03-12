import sys
A, B, C = map(int, sys.stdin.readline().rstrip().split())
sys.stdout.write(
    f'{(A+B)%C}\n'
    f'{((A%C) + (B%C))%C}\n'
    f'{(A*B)%C}\n'
    f'{((A%C) * (B%C))%C}'
)