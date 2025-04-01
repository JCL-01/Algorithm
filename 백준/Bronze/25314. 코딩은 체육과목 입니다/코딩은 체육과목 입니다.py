import sys
byte = int(sys.stdin.readline())
sys.stdout.write('long ' * (byte // 4) + 'int')