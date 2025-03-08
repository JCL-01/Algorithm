def func1(A, B):
    return (A+B)*(A-B)
A, B = map(int, input().split())
print(func1(A, B))