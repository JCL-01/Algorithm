import sys

N = int(sys.stdin.readline())
num_list = []
for _ in range(N):
    num = int(sys.stdin.readline())
    if num == 0:
        num_list.pop()
    else:
        num_list.append(num)
sys.stdout.write(str(sum(num_list)))
    