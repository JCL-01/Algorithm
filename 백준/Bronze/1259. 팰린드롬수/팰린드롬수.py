import sys
*nums, _ = sys.stdin.read().split()
results = []
for num in nums:
    results.append('yes' if num == num[::-1] else 'no')
sys.stdout.write('\n'.join(results))