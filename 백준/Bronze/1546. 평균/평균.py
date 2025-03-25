import sys
N, *scores = map(int, sys.stdin.read().split())
max_score = max(scores)
sum_score = 0
for score in scores:
    sum_score += score / max_score * 100
sys.stdout.write(f'{sum_score / N}')