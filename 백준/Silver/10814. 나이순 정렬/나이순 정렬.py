import sys

mem_list = sys.stdin.readlines()[1:]
mem_list.sort(key=lambda x: int(x.split()[0]))
sys.stdout.write(''.join(mem_list))