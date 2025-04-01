import sys
byte = int(sys.stdin.readline())
for _ in range(byte // 4):
    sys.stdout.write('long ')
sys.stdout.write('int')