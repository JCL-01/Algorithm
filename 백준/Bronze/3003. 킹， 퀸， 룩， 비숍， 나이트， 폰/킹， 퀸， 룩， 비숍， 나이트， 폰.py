import sys
correct_list = [1, 1, 2, 2, 2, 8]
num_list = [num for num in map(int, sys.stdin.readline().split())]
result_list = [x - y for x, y in zip(correct_list, num_list)]
sys.stdout.write(' '.join(map(str, result_list)))