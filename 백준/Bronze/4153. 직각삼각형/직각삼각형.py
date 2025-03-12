import sys
while True:
    try:
        a, b, c = map(int, sys.stdin.readline().split())
    except:
        break
    else:
        len_list = [a, b, c]
        len_list.sort()
        if len_list[0] == 0:
            break
        if len_list[2]**2 == len_list[0]**2 + len_list[1]**2:
            sys.stdout.write("right\n")
        else:
            sys.stdout.write("wrong\n")