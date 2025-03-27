import sys
coord_list = sys.stdin.readlines()[1:]
coord_list.sort(key=lambda x: (int(x.split()[0]), int(x.split()[1])))
sys.stdout.write('\n'.join(map(str.rstrip, coord_list)))