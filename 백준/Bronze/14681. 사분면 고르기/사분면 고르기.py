import sys
x = int(sys.stdin.readline().rstrip())
y = int(sys.stdin.readline().rstrip())
if x > 0 and y > 0:
    sys.stdout.write('1')
elif x < 0 and y > 0:
    sys.stdout.write('2')
elif x < 0 and y < 0:
    sys.stdout.write('3')
elif x > 0 and y < 0:
    sys.stdout.write('4')