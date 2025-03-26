import sys
N = int(sys.stdin.readline())
mem_list = []
for i in range(N):
    age, name = sys.stdin.readline().split()
    mem_list.append((int(age), name, i))
mem_list.sort(key=lambda x:(x[0], x[2]))
for age, name, _ in mem_list:
    sys.stdout.write(f'{age} {name}\n')