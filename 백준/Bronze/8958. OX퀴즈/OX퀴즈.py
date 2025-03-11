N = int(input())
for _ in range(N):
    result = input()
    score = 0
    add_score = 0
    for i in range(len(result)):
        if result[i] == 'O':
            score += 1 + add_score
            add_score += 1
        else:
            add_score = 0
    print(score)