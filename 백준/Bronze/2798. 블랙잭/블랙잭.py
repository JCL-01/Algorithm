import sys
N, M, *num_list = map(int, sys.stdin.read().split())
num_list.sort()
sum_list = []
for i in range(N):
    if num_list[i] * 3 > M:
        break
    for j in range(i + 1, N):
        if num_list[i] + num_list[j] * 2 > M:
            break
        for k in range(j + 1, N):
            if num_list[i] + num_list[j] + num_list[k] > M:
                break
            sum_list.append(num_list[i] + num_list[j] + num_list[k])
sum_list.sort()
sys.stdout.write(f'{sum_list[-1]}')