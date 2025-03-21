import sys
N = int(sys.stdin.readline())
room_num = 1
for i in range(1, 1000000000):
    if N <= room_num:
        sys.stdout.write(str(i))
        break
    room_num += 6 * i