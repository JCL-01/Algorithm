import sys
N, M, *lines = sys.stdin.read().split()
repaint_num_list = []
for start_row in range(int(N) - 7):
    for start_column in range(int(M) - 7):
        W_repaint_num = 0
        B_repaint_num = 0
        for row in range(start_row, start_row + 8):
            for column in range(start_column, start_column + 8):
                if (row + column) % 2 == 0:
                    if lines[row][column] != 'W':
                        W_repaint_num += 1
                    else:
                        B_repaint_num += 1
                else:
                    if lines[row][column] == 'W':
                        W_repaint_num += 1
                    else:
                        B_repaint_num += 1
        repaint_num_list.extend([W_repaint_num, B_repaint_num])
sys.stdout.write(f'{min(repaint_num_list)}')