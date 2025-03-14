import sys 

N, M = map(int, sys.stdin.readline().split())
A, B = [0]*N, [0]*N
sum_arr = [[0]*M for _ in range(N)]
for i in range(N):
    A[i] = list(map(int, sys.stdin.readline().split()))
for i in range(N):
    B[i] = list(map(int, sys.stdin.readline().split()))
for n in range(N):
    for m in range(M):
        sum_arr[n][m] = A[n][m] + B[n][m]
    print(*sum_arr[n])