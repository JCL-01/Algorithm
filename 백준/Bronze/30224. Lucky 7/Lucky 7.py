import sys
N = sys.stdin.readline()
(sys.stdout.write('3') if int(N) % 7 == 0 else sys.stdout.write('2')) if '7' in N else (sys.stdout.write('1') if int(N) % 7 == 0 else sys.stdout.write('0'))