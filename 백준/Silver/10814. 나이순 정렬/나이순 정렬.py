import sys
readline = sys.stdin.readline
N = int(readline())
mem_list = [readline().split() for _ in range(N)]
mem_list.sort(key=lambda x: int(x[0]))
for age, name in mem_list:
    sys.stdout.write(f'{age} {name}\n')