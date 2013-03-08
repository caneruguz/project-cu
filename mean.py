import sys

sum = 0
n = 0
# Another Comment
# Sum input value
for num in open('data.txt'):
  sum += float(num)
  n += 1

print sum / n
