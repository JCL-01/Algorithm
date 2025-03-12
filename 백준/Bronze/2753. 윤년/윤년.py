import sys
year = int(sys.stdin.readline().rstrip())
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 != 0:
            sys.stdout.write('0')
        else:
            sys.stdout.write('1')
    else:
        sys.stdout.write('1')
else:
    sys.stdout.write('0')