import sys

sum = 0
n = 0
# Another Comment

file_name = 'data2.txt'
# Sum input value
for num in open(file_name):
  sum += float(num)
  n += 1

print sum / n
