def func1(A, B):
    return (A+B)*(A-B) if A <= 1000 and B <= 1000 else print('range error')
A, B = map(int, input().split())
print(func1(A, B))