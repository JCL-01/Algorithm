import sys
N = int(sys.stdin.readline())
for _ in range(N):
    A, B = sys.stdin.readline().split()
    sys.stdout.write(str(int(A)+int(B))+'\n')