import sys
N, X = map(int, sys.stdin.readline().split())
num_arr = sys.stdin.readline().split()
small_num_list = []
for i in range(N):
    if int(num_arr[i]) >= X:
        continue
    small_num_list.append(num_arr[i])
print(*small_num_list)