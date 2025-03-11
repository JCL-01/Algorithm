A, B, C = int(input()), int(input()), int(input())
multi = A*B*C
num_str = str(multi)
num_count = {
    '0' : 0,
    '1' : 0,
    '2' : 0,
    '3' : 0,
    '4' : 0,
    '5' : 0,
    '6' : 0,
    '7' : 0,
    '8' : 0,
    '9' : 0
}
for i in num_str:
    num_count[i] += 1
for j in num_count.values():
    print(j)