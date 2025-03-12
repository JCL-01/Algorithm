import sys
T = int(sys.stdin.readline())
for i in range(T):
    H, W, N = map(int, sys.stdin.readline().split())
    if N % H == 0:
        floor_num = str(H)
        room_num = str(N // H)
    else:
        floor_num = str(N % H)
        room_num = str(N // H + 1)
    if int(room_num) < 10:
        room_num = '0' + room_num
    sys.stdout.write(floor_num + room_num)
    if i != T-1:
        sys.stdout.write('\n')