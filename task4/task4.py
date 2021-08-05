import sys

f = sys.argv[1]
file = open(f, 'r')
nums = [int(line) for line in file]

median = sorted(nums)[len(nums) // 2]
print(sum(abs(num - median) for num in nums))
