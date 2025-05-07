import sys
N, M, *lines = sys.stdin.read().split()
repaint_num_list = []
color_opt_list = [('W', 'B'), ('B', 'W')]
for color_opt in color_opt_list:
    for start_row in range(int(N) - 7):
        for start_column in range(int(M) - 7):
            repaint_num = 0
            for row in range(start_row, start_row + 8):
                for column in range(start_column, start_column + 8):
                    if row % 2 == 0:
                        if column % 2 == 0:
                            if lines[row][column] != color_opt[0]:
                                repaint_num += 1
                        else:
                            if lines[row][column] != color_opt[1]:
                                repaint_num += 1
                    else:
                        if column % 2 != 0:
                            if lines[row][column] != color_opt[0]:
                                repaint_num += 1
                        else:
                            if lines[row][column] != color_opt[1]:
                                repaint_num += 1
            repaint_num_list.append(repaint_num)
sys.stdout.write(f'{min(repaint_num_list)}')