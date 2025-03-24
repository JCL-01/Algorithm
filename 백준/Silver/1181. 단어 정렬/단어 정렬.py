import sys
N = int(sys.stdin.readline())
word_set = set()
for word in sys.stdin.read().split():
    word_set.add(word)
result = sorted(word_set, key=lambda x:(len(x), x))
sys.stdout.write('\n'.join(result))