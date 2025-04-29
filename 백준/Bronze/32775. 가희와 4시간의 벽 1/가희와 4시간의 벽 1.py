import sys
S, F = map(int, sys.stdin.read().split())
sys.stdout.write('high speed rail' if S <= F else 'flight')