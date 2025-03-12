import sys

while True:
    try:
        A, B = map(int, sys.stdin.readline().rstrip().split())
    except:
        break
    else:
        print(A+B)